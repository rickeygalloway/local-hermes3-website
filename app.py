from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Ollama API endpoint (runs locally by default)
OLLAMA_API = "http://localhost:11434/api/generate"

@app.route("/", methods=["GET", "POST"])
def home():
    response_text = ""
    user_input = ""
    if request.method == "POST":
        user_input = request.form.get("user_input", "")
        if user_input:
            payload = {
                "model": "hermes3:8b",
                "prompt": user_input,
                "stream": False
            }
            try:
                response = requests.post(OLLAMA_API, json=payload)
                response.raise_for_status()
                raw_response = response.json().get("response", "No response")
                # Replace newlines with <br> tags
                response_text = raw_response.replace("\n", "<br>")
            except requests.exceptions.RequestException as e:
                response_text = f"Error: {str(e)}"
    # Pass response as safe HTML
    return render_template("index.html", response=response_text, user_input=user_input)

if __name__ == "__main__":
    app.run(debug=True)