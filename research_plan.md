---

### 📄 research_plan.md
```markdown
# Research Plan

## Approach
To evaluate whether open-source AI models can support *student competence analysis*, my approach is:
1. *Model Selection*  
   - Review open-source LLMs and NLP models designed for code (e.g., CodeBERT, CodeLlama, SantaCoder).  
   - Shortlist models based on their ability to analyze Python code and generate reflective feedback.  

2. *Evaluation Process*  
   - Test models on *student-written Python snippets* at beginner, intermediate, and advanced levels.  
   - Evaluate their ability to:  
     - Identify syntax errors  
     - Detect logical errors and misconceptions  
     - Suggest reflective prompts instead of giving full solutions  

3. *Validation Criteria*  
   - Quality of generated prompts  
   - Accuracy in identifying misconceptions  
   - Interpretability of responses for students  
   - Computational feasibility (ease of use, resource needs)  

## Initial Thoughts
- *CodeBERT*: Strong at semantic understanding, limited in prompt generation.  
- *CodeLlama*: Excellent at generating explanations/prompts but requires heavy compute.  
- *SantaCoder*: Balanced, lightweight option worth testing.  

Overall, I expect *a hybrid approach* (CodeBERT for analysis + CodeLlama for reflective prompting) to be most effective.