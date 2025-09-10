"""
Helper utilities for loading and saving student code
"""

def load_student_code(filepath: str) -> str:
    with open(filepath, "r") as f:
        return f.read()

def save_feedback(filepath: str, feedback: dict):
    import json
    with open(filepath, "w") as f:
        json.dump(feedback, f, indent=2)