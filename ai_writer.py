from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-base")
model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-base")

def spin_chapter(content):
    prompt = f"Rewrite this creatively while preserving its meaning:\n{content}"
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=512)
    outputs = model.generate(**inputs, max_new_tokens=400, temperature=0.7)
    result = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return result
