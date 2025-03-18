from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Ollama API endpoint (runs locally)
OLLAMA_API = "http://localhost:11434/api/generate"

# Store conversation history
conversation_history = []

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        user_input = request.form.get("user_input", "")
        if user_input:
            # Send request to Ollama
            payload = {
                "model": "hermes3:8b",
                "prompt": user_input,
                "stream": False
            }
            try:
                response = requests.post(OLLAMA_API, json=payload)
                response.raise_for_status()
                response_text = response.json().get("response", "No response")
                # Add to conversation history
                conversation_history.append({"user": user_input, "bot": response_text})
            except requests.exceptions.RequestException as e:
                conversation_history.append({"user": user_input, "bot": f"Error: {str(e)}"})
    return render_template("index.html", conversation=conversation_history)

if __name__ == "__main__":
    app.run(debug=True)