from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from langchain_groq import ChatGroq
import os

# Check tools documentation for more information on how to use them
from .tools.math_ex import MathExTool

# Initialize tools
# profiler_tool = ProfilerTool()
math_ex_tool = MathExTool()
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

    @agent
    def profiler_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['profiler_agent'],
            llm=self.groq_llm,
            # tools=[profiler_tool],
            verbose=True
        )

    @agent
    def exercise_generator_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['exercise_generator_agent'],
            llm=self.groq_llm,
            tools=[math_ex_tool],
            verbose=True
        )

    @agent
    def selector_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['selector_agent'],
            llm=self.groq_llm,
            # tools=[test_composer_tool],
            verbose=True
        )

    @agent
    def evaluator_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['evaluator_agent'],
            llm=self.groq_llm,
            # tools=[answer_checker_tool],
            verbose=True
        )

    @agent
    def report_filer_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['report_filer_agent'],
            llm=self.groq_llm,
            # tools=[report_filer_tool],
            verbose=True
        )

    @task
    def profile_creation_task(self) -> Task:
        return Task(
            config=self.tasks_config['profile_creation'],
            agent=self.profiler_agent()
        )

    @task
    def exercise_generation_task(self) -> Task:
        return Task(
            config=self.tasks_config['exercise_generation'],
            agent=self.exercise_generator_agent()
        )

    @task
    def exercise_selection_composition_task(self) -> Task:
        return Task(
            config=self.tasks_config['exercise_selection_composition'],
            agent=self.selector_agent()
        )

    @task
    def answer_evaluation_task(self) -> Task:
        return Task(
            config=self.tasks_config['answer_evaluation'],
            agent=self.evaluator_agent()
        )

    @task
    def report_filing_task(self) -> Task:
        return Task(
            config=self.tasks_config['report_filing'],
            agent=self.report_filer_agent()
        )

    @crew
    def crew(self) -> Crew:
        """Create and manage the math tutoring crew."""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True
        )
