from transformers import AutoTokenizer, AutoModelForCausalLM
import os

model_id = "deepseek-ai/deepseek-coder-1.3b-instruct"
save_path = "./models/deepseek-coder-1.3b"

print("📥 Downloading model and tokenizer...")

tokenizer = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(model_id, trust_remote_code=True)

os.makedirs(save_path, exist_ok=True)
tokenizer.save_pretrained(save_path)
model.save_pretrained(save_path)

print("✅ Model and tokenizer saved to:", save_path)
