"""
Evaluate student-written Python code with selected model
"""

def evaluate_code_with_model(code: str, model_name: str):
    print(f"Evaluating with {model_name}...")
    if model_name == "CodeBERT":
        return {"feedback": "Possible missing colon or incorrect loop structure"}
    elif model_name == "CodeLlama":
        return {"feedback": "What happens when n=0 in your recursive function?"}
    else:
        return {"feedback": "Model not implemented"}

if _name_ == "_main_":
    student_code = "def factorial(n): return n * factorial(n-1)"
    result = evaluate_code_with_model(student_code, "CodeLlama")
    print(result)