from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from langchain_groq import ChatGroq
import os

# Check tools documentation for more information on how to use them
from .tools.level1_math import Level1Math
from .tools.user_input_tool import UserInputTool

# Initialize tools
# profiler_tool = ProfilerTool()
math_ex_tool = Level1Math()
user_input_tool = UserInputTool()
# test_composer_tool = TestComposerTool()
# answer_checker_tool = AnswerCheckerTool()
# report_filer_tool = ReportFilerTool()

groq_api_key = os.getenv('GROQ_API_KEY')


@CrewBase
class MathTutorCrew:
    """Math Tutor Crew for educating children aged 5 to 12."""
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    def __init__(self) -> None:
        self.groq_llm = ChatGroq(temperature=0, groq_api_key=groq_api_key, model_name="llama3-70b-8192")

    # @agent
    # def profiler_agent(self) -> Agent:
    #     return Agent(
    #         config=self.agents_config['profiler_agent'],
    #         llm=self.groq_llm,
    #         # tools=[profiler_tool],
    #         verbose=True
    #     )

    @agent
    def tutor_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['Tutor_agent'],
            llm=self.groq_llm,
            memory=False,
            max_iter=1,
            verbose=True
        )

    # @agent
    # def selector_agent(self) -> Agent:
    #     return Agent(
    #         config=self.agents_config['selector_agent'],
    #         llm=self.groq_llm,
    #         # tools=[test_composer_tool],
    #         verbose=True
    #     )
    #
    # @agent
    # def evaluator_agent(self) -> Agent:
    #     return Agent(
    #         config=self.agents_config['evaluator_agent'],
    #         llm=self.groq_llm,
    #         # tools=[answer_checker_tool],
    #         verbose=True
    #     )
    #
    # @agent
    # def report_filer_agent(self) -> Agent:
    #     return Agent(
    #         config=self.agents_config['report_filer_agent'],
    #         llm=self.groq_llm,
    #         # tools=[report_filer_tool],
    #         verbose=True
    #     )

    # @task
    # def profile_creation_task(self) -> Task:
    #     return Task(
    #         id='profile_creation',
    #         config=self.tasks_config['profile_creation'],
    #         agent=self.profiler_agent(),
    #         next_task='exercise_generation'
    #     )

    @task
    def exercise_generation_task(self) -> Task:
        return Task(
            config=self.tasks_config['exercise_generation'],
            agent=self.tutor_agent(),
            tools=[math_ex_tool]
        )

    @task
    def collect_user_answer(self) -> Task:
        return Task(
            config=self.tasks_config['collect_user_answer'],
            agent=self.tutor_agent(),
            tools=[user_input_tool],
            user_input=True
        )

    @task
    def answer_evaluation_task(self) -> Task:
        return Task(
            config=self.tasks_config['answer_evaluation'],
            agent=self.tutor_agent(),
        )
    #
    # @task
    # def report_filing_task(self) -> Task:
    #     return Task(
    #         id='report_filing',
    #         config=self.tasks_config['report_filing'],
    #         agent=self.report_filer_agent(),
    #         # next_task=''
    #     )

    @crew
    def crew(self) -> Crew:
        """Create and manage the math tutoring crew."""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=False
        )
