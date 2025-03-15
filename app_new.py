from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# External API endpoint
API_URL = "https://redactedDomain.com/v1/completions"

@app.route("/", methods=["GET", "POST"])
def home():
    response_text = ""
    user_input = ""
    if request.method == "POST":
        user_input = request.form.get("user_input", "")
        if user_input:
            # Prepare the payload for the API
            payload = {
                "model": "NousResearch/Hermes-3-Llama-3.1-8B",
                "prompt": user_input,
                "max_tokens": 100,
                "temperature": 0
            }
            try:
                # Make the POST request to the external API
                response = requests.post(
                    API_URL,
                    headers={"Content-Type": "application/json"},
                    json=payload
                )
                response.raise_for_status()  # Raise an error for bad status codes
                # Extract the text from the API response (adjust based on actual response structure)
                response_text = response.json().get("choices", [{}])[0].get("text", "No response")
            except requests.exceptions.RequestException as e:
                response_text = f"Error: {str(e)}"
    return render_template("index.html", response=response_text, user_input=user_input)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)  # Use port 5001 to avoid conflict with app.py