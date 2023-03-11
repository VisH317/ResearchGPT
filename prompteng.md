## prompt engineering MVP pipeline
_Objective:_ Create a program to accept a list of prompts and an objective, and evaluate each prompt based on the objective to find the optimal prompt

**Required Parts:**
 * Need to run on the model - can be done using OpenAI API
 * Need to evaluate the outputs using the objective
   * Zero-shot learning techniques are important here: 
   * Comparative NLP techniques, pretrained models to generate prompts based on general ideas
 * Training pipeline for fine-tuning: need to be able to compare an objective to the actual prompt output and evaluate it