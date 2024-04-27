from crewai_tools import BaseTool
import sympy as sp
import random


class Level1Math(BaseTool):
    name: str = "Math Problem Generator Tool"
    description: str = "Generate math problems."

    # def _run(self, level: str, history: dict) -> dict:
    #     if level == 'Level 1':
    #         ex_type = random.choice(['counting', 'add_&_sub', 'symbol'])
    #         if ex_type == 'counting':
    def _run(self) -> dict:
                step = random.choice([1, -1, 2, -2, 5, -5, 10, -10, 20])
                if step == -1:
                    start_number = random.randint(10, 100)
                elif step == -2:
                    start_number = random.randint(20, 100)
                elif step == -5:
                    start_number = random.randint(50, 100)
                elif step == -10:
                    start_number = random.randint(90, 200)
                else:
                    start_number = random.randint(1, 100)
                end_number = start_number + 10 * step
                """
                Generates a sequence of numbers for counting exercises.
            
                Parameters:
                - start_number (int): The number to start counting from.
                - end_number (int): The number to count to (inclusive if within range after steps).
                - step (int): The step size to use for counting (can be positive or negative).
            
                Returns:
                - {'problem': problem, 'solution': solution} formatted question with answer
                """
                # Determine the sequence based on step being positive or negative
                def sequence(_start_number, _end_number, _step):
                    if step > 0:
                        return list(range(start_number, end_number + 1, step))
                    else:
                        return list(range(start_number, end_number - 1, step))

                # Generate a sequence of numbers
                numbers = sequence(start_number, end_number, step)
                # replace one random number with a question mark
                question_index = random.randint(0, len(numbers) - 1)
                numbers[question_index] = '?'
                # Generate the problem and solution
                problem = f"What is the missing number in the sequence: {numbers}"
                solution = start_number + question_index * step
                return {'problem': problem, 'solution': solution}
