# Reproducing Llama 3 Instruct Arithmetic & GSM8K Performance

This repository contains the companion code for two tutorial posts on Medium:

- (How to Use Llama 3 Instruct on Hugging Face)[https://medium.com/@sewoong.lee/how-to-reproduce-llama-3s-performance-on-gsm-8k-e0dce7fe9926]
- (How to Reproduce Llama-3's Performance on GSM-8k)[https://medium.com/@sewoong.lee/how-to-reproduce-llama-3s-performance-on-gsm-8k-e0dce7fe9926]

It shows how to:

1. Load **Meta-Llama-3-8B-Instruct** from Hugging Face with 4-bit quantization (BitsAndBytes).
2. Use **chat templating** in `transformers` to run multi-turn conversations.
3. Evaluate Llama-3 on **GSM8K** with few-shot, chain-of-thought prompting and reproduce the ~78% accuracy reported by Meta.
