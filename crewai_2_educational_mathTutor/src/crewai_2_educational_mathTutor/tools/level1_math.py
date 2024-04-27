from crewai_tools import BaseTool
import random


class Level1Math(BaseTool):
    name: str = "Math Problem Generator Tool"
    description: str = "Generate simple math problems for level one mathematics."

    def _run(self):
        # Choose the type of exercise
        exercise_type = random.choice(['count', 'addition', 'subtraction'])

        if exercise_type == 'count':
            return self.generate_counting_exercise()
        elif exercise_type == 'addition':
            return self.generate_addition_exercise()
        elif exercise_type == 'subtraction':
            return self.generate_subtraction_exercise()

    def generate_counting_exercise(self):
        # Generate a counting sequence with a missing number
        start = random.randint(1, 10)
        sequence = list(range(start, start + 10))
        missing_index = random.randint(1, len(sequence) - 2)
        solution = sequence[missing_index]
        sequence[missing_index] = '?'
        problem = f"Complete the sequence: {sequence}"
        return {'problem': problem, 'solution': solution}

    def generate_addition_exercise(self):
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        solution = num1 + num2
        problem = f"What is {num1} + {num2}?"
        return {'problem': problem, 'solution': solution}

    def generate_subtraction_exercise(self):
        num1 = random.randint(1, 10)
        num2 = random.randint(1, num1)  # Ensure the result is non-negative
        solution = num1 - num2
        problem = f"What is {num1} - {num2}?"
        return {'problem': problem, 'solution': solution}
