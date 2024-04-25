from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from langchain_groq import ChatGroq
import os
# Check our tools documentations for more information on how to use them
from crewai_tools import SerperDevTool

from crewai_2_educational_mathTutor.src.crewai_2_educational_mathTutor.tools.custom_tool import DatabaseTool, \
    SpeechTool, EducationalTool, ExerciseCreatorTool, SolutionCheckerTool


groq_api_key = os.getenv('GROQ_API_KEY')

# Create an instance of SerperDevTool
serper_dev_tool = SerperDevTool()

# Initialize tools
db_tool = DatabaseTool()
speech_tool = SpeechTool()
education_tool = EducationalTool()
exercise_tool = ExerciseCreatorTool()
solution_tool = SolutionCheckerTool()


@CrewBase
class MathTutor():
    """MathTutor crew"""
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    def __init__(self) -> None:
        self.groq_llm = ChatGroq(temperature=0, groq_api_key=groq_api_key, model_name="llama3-70b-8192")

    @agent
    def profile_manager(self) -> Agent:
        return Agent(
            config=self.agents_config['profile_manager'],
            llm=self.groq_llm,
            tools=[db_tool],
            verbose=True
        )

    @agent
    def communicator(self) -> Agent:
        return Agent(
            config=self.agents_config['communicator'],
            llm=self.groq_llm,
            tools=[speech_tool],
            verbose=True
        )

    @agent
    def exercise_generator(self) -> Agent:
        return Agent(
            config=self.agents_config['exercise_generator'],
            llm=self.groq_llm,
            tools=[education_tool],
            verbose=True
        )

    @agent
    def grader(self) -> Agent:
        return Agent(
            config=self.agents_config['grader'],
            llm=self.groq_llm,
            tools=[education_tool],
            verbose=True
        )

    @agent
    def feedback_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['feedback_analyst'],
            llm=self.groq_llm,
            tools=[db_tool],
            verbose=True
        )

    @task
    def profile_task(self) -> Task:
        return Task(
            config=self.tasks_config['profile_task'],
            agent=self.profile_manager()
        )

    @task
    def communication_task(self) -> Task:
        return Task(
            config=self.tasks_config['communication_task'],
            agent=self.communicator(),
        )

    @task
    def exercise_task(self) -> Task:
        return Task(
            config=self.tasks_config['exercise_task'],
            agent=self.exercise_generator(),
        )

    @task
    def grading_task(self) -> Task:
        return Task(
            config=self.tasks_config['grading_task'],
            agent=self.grader(),
        )

    @task
    def feedback_task(self) -> Task:
        return Task(
            config=self.tasks_config['feedback_task'],
            agent=self.feedback_analyst(),
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Crewai1 crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=2,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
