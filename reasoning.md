# Reasoning

## What makes a model suitable for high-level competence analysis?
- Ability to parse *syntax and semantics* of Python code  
- Detecting *conceptual gaps* (e.g., missing base case in recursion)  
- Generating *pedagogical feedback* that encourages thinking rather than spoon-feeding solutions  
- Lightweight enough to integrate in educational platforms  

## How would you test whether a model generates meaningful prompts?
1. Provide it with *incorrect student code*.  
2. Check if it generates *open-ended, reflective prompts* like:  
   - “Why does your recursion stop?”  
   - “What happens when n=0?”  
3. Compare against ground-truth prompts designed by human instructors.  
4. Evaluate with a small group of learners for *pedagogical usefulness*.  

## What trade-offs might exist?
- *Accuracy vs Interpretability*: Highly accurate models may still give overly complex outputs.  
- *Cost vs Accessibility*: Larger models require GPUs, which may not be affordable for schools.  
- *Generality vs Specificity*: A generic LLM may miss common beginner mistakes, while a domain-trained model might overfit.  

## Why choose the evaluated model?
- *CodeBERT*: Chosen for lightweight analysis of student code. Strengths: semantic analysis, good for classification. Limitation: poor prompt generation.  
- *CodeLlama*: Chosen for reflective feedback generation. Strengths: explanations & prompts. Limitation: may provide full solutions, high resource cost.  
- *SantaCoder*: Considered as middle ground, lightweight but less powerful.