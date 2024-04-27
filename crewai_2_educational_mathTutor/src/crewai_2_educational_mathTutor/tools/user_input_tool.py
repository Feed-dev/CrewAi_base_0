from crewai_tools import BaseTool


class UserInputTool(BaseTool):
    name: str = "UserInputTool"
    description: str = "A tool to prompt user for input and collect their responses."

    def _run(self, prompt: str) -> str:
        # Here, you would implement the method to capture user input.
        # This is a placeholder for user input simulation.
        user_response = input(prompt)  # Using Python's built-in input function
        return user_response
