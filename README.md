# Reproducing Llama 3 Instruct Arithmetic & GSM8K Performance

This repository contains the companion code for two tutorial posts:

- **How to Use Llama 3 Instruct on Hugging Face**  
- **How to Reproduce Llama-3's Performance on GSM-8k**

It shows how to:

1. Load **Meta-Llama-3-8B-Instruct** from Hugging Face with 4-bit quantization (BitsAndBytes).
2. Use **chat templating** in `transformers` to run multi-turn conversations.
3. Evaluate Llama-3 on **GSM8K** with few-shot, chain-of-thought prompting and reproduce the ~78% accuracy reported by Meta.
