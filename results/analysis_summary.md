# Model Evaluation Summary

## CodeBERT
- Strengths: Strong at code classification, detecting syntax/semantic issues
- Weaknesses: Poor at reflective prompt generation

## CodeLlama
- Strengths: Generates reflective prompts, encourages deeper learning
- Weaknesses: Tends to give full solutions, heavy compute needs

## SantaCoder
- Balanced option for lightweight use
- Slightly weaker on pedagogy compared to CodeLlama

## Conclusion
A *hybrid approach* is best:  
- Use *CodeBERT* for code analysis and error detection  
- Use *CodeLlama* for reflective prompt generation