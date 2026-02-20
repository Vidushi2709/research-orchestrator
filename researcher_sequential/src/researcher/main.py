#!/usr/bin/env python
import sys
import warnings
import os

# Add the src directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from dotenv import load_dotenv
load_dotenv()

from researcher.crew import Researcher

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': 'AI Agents in Healthcare',  # Change this to research any topic
        'current_year': 2026,
        'user_name': 'Vin',
        'user_role': 'AI Engineer', 
        'user_location': 'Mars',
        'user_preferences': 'Focus on practical implementations, prefer open-source solutions, interested in cost-effective approaches'
    }
    
    try:
        result = Researcher().crew().kickoff(inputs=inputs)
        print("\n\n========================")
        print("## Crew Execution Complete!")
        print("========================\n")
        print("Results:")
        print(result)
        return result
    except Exception as e:
        print(f"An error occurred: {e}")
        raise e


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        'topic': 'AI Agents in Healthcare',
        'current_year': 2026,
        'user_name': 'Vin',
        'user_role': 'AI Engineer', 
        'user_location': 'Mars',
        'user_preferences': 'Focus on practical implementations, prefer open-source solutions, interested in cost-effective approaches'
    }
    try:
        Researcher().crew().train(
            n_iterations=int(sys.argv[1]), 
            filename=sys.argv[2], 
            inputs=inputs
        )
    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")


def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        Researcher().crew().replay(task_id=sys.argv[1])
    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")


def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        'topic': 'AI Agents in Healthcare',
        'current_year': 2026,
        'user_name': 'Vin',
        'user_role': 'AI Engineer', 
        'user_location': 'Mars',
        'user_preferences': 'Focus on practical implementations, prefer open-source solutions, interested in cost-effective approaches'
    }
    try:
        Researcher().crew().test(
            n_iterations=int(sys.argv[1]), 
            openai_model_name=sys.argv[2], 
            inputs=inputs
        )
    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")


if __name__ == "__main__":
    run()