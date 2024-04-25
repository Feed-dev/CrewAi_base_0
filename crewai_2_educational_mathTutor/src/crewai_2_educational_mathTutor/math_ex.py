import sympy as sp
import random


def generate_addition_problem(level):
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
    return sp.latex(expr), num1 + num2  # returns the LaTeX form of the problem and the solution


def generate_subtraction_problem(level):
    if level == 'easy':
        num1 = random.randint(1, 10)
        num2 = random.randint(1, num1)  # ensure the result is non-negative
    elif level == 'medium':
        num1 = random.randint(10, 100)
        num2 = random.randint(1, num1)
    else:  # assuming hard level
        num1 = random.randint(100, 1000)
        num2 = random.randint(1, num1)

    expr = sp.Add(num1, -num2, evaluate=False)  # Use Add for proper formatting
    return sp.latex(expr), num1 - num2


def generate_multiplication_problem(level):
    if level == 'easy':
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
    elif level == 'medium':
        num1 = random.randint(10, 50)
        num2 = random.randint(1, 10)
    else:  # assuming hard level
        num1 = random.randint(50, 100)
        num2 = random.randint(1, 50)

    expr = sp.Mul(num1, num2, evaluate=False)
    return sp.latex(expr), num1 * num2


def generate_division_problem(level):
    if level == 'easy':
        num1 = random.randint(1, 10) * random.randint(1, 10)
        num2 = random.randint(1, 10)
    elif level == 'medium':
        num1 = random.randint(10, 50) * random.randint(1, 10)
        num2 = random.randint(1, 10)
    else:  # assuming hard level
        num1 = random.randint(50, 100) * random.randint(1, 50)
        num2 = random.randint(1, 50)

    expr = sp.Rational(num1, num2)  # To show division as a fraction
    return sp.latex(expr), num1 / num2


# Example usage:
add_problem, add_solution = generate_addition_problem('easy')
sub_problem, sub_solution = generate_subtraction_problem('easy')
mul_problem, mul_solution = generate_multiplication_problem('easy')
div_problem, div_solution = generate_division_problem('easy')

print("Addition Problem:", add_problem, "Solution:", add_solution)
print("Subtraction Problem:", sub_problem, "Solution:", sub_solution)
print("Multiplication Problem:", mul_problem, "Solution:", mul_solution)
print("Division Problem:", div_problem, "Solution:", div_solution)
