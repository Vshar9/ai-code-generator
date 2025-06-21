from flask import Flask, request, jsonify, render_template
from transformers import pipeline
import torch
import re
app = Flask(__name__, template_folder="templates", static_folder="static")
generator = None
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/generate", methods=["POST"])
def generate_code():
    global generator
    if generator is None:
        return jsonify({"error": "Model not initialized"}), 500
    user_prompt = request.form.get("prompt", "").strip()
    if not user_prompt:
        return jsonify({"error": "Prompt is empty"}), 400
    print(f"⚡ Prompt: {user_prompt}")
    engineered_prompt = f"{user_prompt.strip()}\nWrite only the code and nothing else. Do not add tests or comments as well."
    result = generator(engineered_prompt, max_new_tokens=256, do_sample=True, temperature=0.7)
    output = result[0]["generated_text"]
    cleaned_output = output.replace(engineered_prompt, "").strip()
    match = re.search(r"```(?:\w*\n)?([\s\S]+?)```", cleaned_output)
    code_only = match.group(1).strip() if match else cleaned_output
    return jsonify({"code": code_only})

if __name__ == "__main__":
    print("📦 Loading DeepSeek-Coder model from disk...")
    MODEL_PATH = "./models/deepseek-coder-1.3b"
    device = 0 if torch.cuda.is_available() else -1

    generator = pipeline(
        "text-generation",
        model=MODEL_PATH,
        tokenizer=MODEL_PATH,
        trust_remote_code=True,
        device=device
    )
    app.run(host="0.0.0.0", port=5000, debug=True)
