from crewai_tools import BaseTool


class MyCustomTool(BaseTool):
    name: str = "Name of my tool"
    description: str = "Clear description for what this tool is useful for, you agent will need this information to use it."

    def _run(self, argument: str) -> str:
        # Implementation goes here
        return "this is an example of a tool output, ignore it and move along."


class ExerciseCreatorTool(BaseTool):
    name = "Exercise Creator"
    description = "Generates personalized math exercises based on the user's skill level."

    def _run(self, topic: str, level: str) -> dict:
        # Logic to generate exercises
        # This is a placeholder; actual implementation would depend on specific requirements
        return {
            "exercise": "Solve for x: 2x + 3 = 15",
            "answer": 6
        }


class SolutionCheckerTool(BaseTool):
    name = "Solution Checker"
    description = "Checks the solutions submitted by users and provides grades."

    def _run(self, submitted_answer: int, correct_answer: int) -> str:
        # Compare the submitted answer with the correct one
        if submitted_answer == correct_answer:
            return "Correct"
        else:
            return "Incorrect, please try again"


class DatabaseTool:
    pass


class SpeechTool:
    pass


class EducationalTool:
    pass