from crewai_tools import BaseTool
import sympy as sp
import random


class MathExTool(BaseTool):
    name: str = "Math Problem Generator Tool"
    description: str = "Generates addition math problems and returns them in LaTeX format along with solutions."

    def _run(self, level: str) -> dict:
        """Generates an addition problem based on the specified difficulty level.

        Args:
            level (str): Difficulty level of the problem ('easy', 'medium', 'hard').

        Returns:
            dict: A dictionary containing the LaTeX representation of the problem and its solution.
        """
        if level == 'easy':
            num1 = random.randint(1, 10)
            num2 = random.randint(1, 10)
        elif level == 'medium':
            num1 = random.randint(10, 100)
            num2 = random.randint(10, 100)
        else:  # assuming hard level
            num1 = random.randint(100, 1000)
            num2 = random.randint(100, 1000)

        # Create a symbolic expression
        expr = sp.Add(num1, num2, evaluate=False)
        # Return the LaTeX form of the problem and the solution
        return {"problem": sp.latex(expr), "solution": num1 + num2}
