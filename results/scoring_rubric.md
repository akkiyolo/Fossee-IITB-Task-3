# Scoring Rubric for Model Evaluation

Each model is evaluated on *three key dimensions*:  

1. *Accuracy (0–5)*  
   - How well the model detects real errors or misconceptions in code.  
   - 0 = Incorrect or irrelevant feedback  
   - 5 = Precise and correct error identification  

2. *Interpretability (0–5)*  
   - How clear and understandable the model’s feedback is.  
   - 0 = Confusing/technical  
   - 5 = Student-friendly and easy to follow  

3. *Pedagogical Value (0–5)*  
   - Does the feedback encourage deeper learning?  
   - 0 = Gives away solution directly / irrelevant feedback  
   - 5 = Reflective prompts that guide learning  

---

## Scores by Example

| Model       | Level        | Accuracy | Interpretability | Pedagogical Value | Notes |
|-------------|-------------|----------|------------------|-------------------|-------|
| *CodeBERT* | Beginner    | 5        | 4                | 2                 | Correctly identified missing colon, but feedback was direct not reflective |
|             | Intermediate| 4        | 3                | 2                 | Detected missing base case, but explanation lacked guidance |
|             | Advanced    | 4        | 3                | 2                 | Flagged recursion & decorator issues, but no reflective learning prompts |
| *CodeLlama*| Beginner    | 4        | 5                | 5                 | Asked reflective question about colon, very student-friendly |
|             | Intermediate| 4        | 5                | 5                 | Prompt encouraged thinking (“What happens when n=0?”) |
|             | Advanced    | 4        | 4                | 5                 | Generated reflective questions on recursion, class design, decorators |

---

## Overall Scores (Averaged)

| Model       | Accuracy | Interpretability | Pedagogical Value | Overall (avg) |
|-------------|----------|------------------|-------------------|---------------|
| *CodeBERT* | 4.3      | 3.3              | 2.0               | 3.2           |
| *CodeLlama*| 4.0      | 4.7              | 5.0               | 4.6           |

---

## Insights
- *CodeBERT* is best for raw accuracy and error detection, but lacks pedagogical finesse.  
- *CodeLlama* shines in student-friendly reflective prompting, making it better for competence analysis.  
- *Hybrid Approach: Using CodeBERT for **error detection* + CodeLlama for *feedback generation* yields the strongest system.