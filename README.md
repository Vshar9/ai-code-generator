# 🧠 AI Code Generator

A lightweight Flask-based web app that generates Python code from natural language prompts using the `deepseek-coder-1.3b` model.

## 🚀 Features

- Clean and minimal web UI
- Generates Python code using Hugging Face Transformers
- Model loads only once for fast inference
- Extracts only code output (no extra explanations)
- Works offline after model download

## 📁 Project Structure

```
intern-project/
├── app.py                  # Main Flask app
├── downloader-script.py    # Optional script to download the model
├── requirements.txt        # Python dependencies
├── models/
│   └── deepseek-coder-1.3b/  # Local model directory
├── templates/
│   └── index.html          # Frontend form
├── static/
│   └── styles.css          # Basic styles
```

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd intern-project
```

### 2. Set Up Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate    # On Windows
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Download the Model

Manually download `deepseek-coder-1.3b` from:  
https://huggingface.co/deepseek-ai/deepseek-coder-1.3b

Place it in:

```
./models/deepseek-coder-1.3b/
```

## ▶️ Run the Application

```bash
python app.py
```

Then visit [http://localhost:5000](http://localhost:5000) in your browser.

## ✅ Requirements

### Software

- Python 3.10+
- Flask
- transformers >= 4.36
- torch

### Hardware

- CPU (8GB RAM minimum)
- GPU (recommended for faster generation)

## 🧪 Example Prompt

```
Write a Python function to calculate factorial.
```

✅ Output:

```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
```

## 📄 License

MIT License

## 🙏 Acknowledgements

- Hugging Face 🤗
- DeepSeek Coder Model