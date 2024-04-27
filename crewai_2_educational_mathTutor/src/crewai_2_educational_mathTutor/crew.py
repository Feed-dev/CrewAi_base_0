from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from langchain_groq import ChatGroq
import os

from .tools.level1_math import Level1Math
from .tools.user_input_tool import UserInputTool

math_ex_tool = Level1Math()
user_input_tool = UserInputTool()


groq_api_key = os.getenv('GROQ_API_KEY')


@CrewBase
class MathTutorCrew:
    """Math Tutor Crew for educating children aged 5 to 12."""
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    def __init__(self) -> None:
        self.groq_llm = ChatGroq(temperature=0, groq_api_key=groq_api_key, model_name="llama3-70b-8192")


    @agent
    def tutor_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['Tutor_agent'],
            llm=self.groq_llm,
            memory=False,
            max_iter=3,
            verbose=True
        )

    @task
    def exercise_generation_task(self) -> Task:
        return Task(
            config=self.tasks_config['exercise_generation'],
            agent=self.tutor_agent(),
            tools=[math_ex_tool],
            execute=self.generate_exercise  # Method to handle exercise generation
        )

    def generate_exercise(self, inputs):
        # This method would be called by the task, leveraging the Level1Math tool
        # 'inputs' could include any additional parameters if necessary
        exercise_output = math_ex_tool._run()
        return exercise_output

    @task
    def collect_user_answer(self) -> Task:
        return Task(
            config=self.tasks_config['collect_user_answer'],
            agent=self.tutor_agent(),
            tools=[user_input_tool],
            execute=self.collect_answer
        )

    def collect_answer(self, inputs):
        prompt = inputs['problem']  # Ensure 'problem' is passed correctly
        user_response = user_input_tool._run(prompt=prompt)
        return {'user_response': user_response, 'correct_answer': inputs['solution']}

    @task
    def answer_evaluation_task(self) -> Task:
        return Task(
            config=self.tasks_config['answer_evaluation'],
            agent=self.tutor_agent(),
        )

    @crew
    def crew(self) -> Crew:
        """Create and manage the math tutoring crew."""
        # Initialize tasks
        exercise_task = self.exercise_generation_task()
        user_input_task = self.collect_user_answer()
        evaluation_task = self.answer_evaluation_task()

        return Crew(
            agents=[self.tutor_agent()],
            tasks=[exercise_task, user_input_task, evaluation_task],
            process=Process.sequential,
            verbose=True
        )
