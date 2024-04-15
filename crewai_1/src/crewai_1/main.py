#!/usr/bin/env python
from crewai_1.crew import Crewai1Crew


def run():
    # Replace with your inputs, it will automatically interpolate any tasks and agents information
    inputs = {
        'topic': 'AI LLMs'
    }
    Crewai1Crew().crew().kickoff(inputs=inputs)