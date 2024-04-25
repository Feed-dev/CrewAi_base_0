#!/usr/bin/env python
from crewai_2_educational_mathTutor.src.crewai_2_educational_mathTutor.crew import MathTutor


def run():
    # Replace with your inputs, it will automatically interpolate any tasks and agents information
    inputs = {
        'topic': input("Enter the topic for the exercise: "),
    }
    MathTutor().crew().kickoff(inputs=inputs)


if __name__ == '__main__':
    run()
