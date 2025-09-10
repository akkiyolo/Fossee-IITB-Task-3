# CodeBERT Notes

- *Model*: microsoft/codebert-base
- *Type*: Transformer-based model (RoBERTa pretraining on code)
- *Focus*: Code understanding, classification, and semantic analysis

## Strengths
- Good at identifying *syntax and semantic patterns*
- Can detect *incorrect constructs* in student Python code
- Lightweight compared to large generative models

## Weaknesses
- Not designed for *generating prompts or questions*
- Limited in handling long contextual reasoning

## Use Case for Competence Analysis
- Detects *logical errors* in Python code
- Useful as a “code reviewer” in automated education systems