from crewai_tools import BaseTool
import sympy as sp
import random


class MathExTool(BaseTool):
    name: str = "Math Problem Generator Tool"
    description: str = "Generate math problems based on the difficulty level."

    def _run(self, level: str, num_problems: int = 1) -> dict:
        """
        Generates a specified number of math problems based on the difficulty level.

        Args:
            level (str): Difficulty level of the problems ('easy', 'medium', 'hard').
            num_problems (int): The number of math problems to generate.

        Returns:
            dict: A dictionary containing lists of LaTeX representations of the problems and their solutions.
        """
        problems = []
        solutions = []
        for _ in range(num_problems):
            # choose a random item out of a list
            ex_type = random.choice(['addition', 'subtraction', 'multiplication', 'division'])
            if ex_type == 'addition':
                # Generate two random numbers based on the difficulty level
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
                problems.append(sp.latex(expr))
                solutions.append(num1 + num2)

            if ex_type == 'subtraction':
                if level == 'easy':
                    num1 = random.randint(1, 10)
                    num2 = random.randint(1, num1)  # ensure the result is non-negative
                elif level == 'medium':
                    num1 = random.randint(10, 100)
                    num2 = random.randint(1, num1)
                else:  # assuming hard level
                    num1 = random.randint(100, 1000)
                    num2 = random.randint(1, num1)

                # Create a symbolic expression
                expr = sp.Add(num1, -num2, evaluate=False)
                problems.append(sp.latex(expr))
                solutions.append(num1 - num2)

            if ex_type == 'multiplication':
                if level == 'easy':
                    num1 = random.randint(1, 10)
                    num2 = random.randint(1, 10)
                elif level == 'medium':
                    num1 = random.randint(10, 50)
                    num2 = random.randint(1, 10)
                else:  # assuming hard level
                    num1 = random.randint(50, 100)
                    num2 = random.randint(1, 50)

                # Create a symbolic expression
                expr = sp.Mul(num1, num2, evaluate=False)
                problems.append(sp.latex(expr))
                solutions.append(num1 * num2)

            if ex_type == 'division':
                if level == 'easy':
                    num2 = random.randint(1, 10)
                    num1 = num2 * random.randint(1, 10)
                elif level == 'medium':
                    num2 = random.randint(1, 10)
                    num1 = num2 * random.randint(10, 50)
                else:  # assuming hard level
                    num2 = random.randint(1, 50)
                    num1 = num2 * random.randint(50, 100)

                # Create a symbolic expression
                expr = sp.Mul(num1, sp.Pow(num2, -1), evaluate=False)
                problems.append(sp.latex(expr))
                solutions.append(num1 / num2)

        # Return the LaTeX forms of the problems and the solutions
        return {"problems": problems, "solutions": solutions}
