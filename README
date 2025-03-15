# Local Hermes3:8B Website

A simple local website built with Flask, Ollama, and VS Code on Windows. It uses the `hermes3:8b` model to answer questions typed into a webpage, all running offline on your machine.

## Setup Steps
1. **Install VS Code**
   - Download and install from [code.visualstudio.com](https://code.visualstudio.com/).

2. **Install Python**
   - Download Python 3.11 or 3.12 from [python.org](https://www.python.org/downloads/windows/).
   - Check "Add Python to PATH" during installation.
   - Verify: Open Command Prompt and run `python --version`.

3. **Install Ollama**
   - Download from [ollama.com](https://ollama.com/download) and run the installer.
   - Verify: In Command Prompt, run `ollama --version`.

4. **Download the Hermes3:8B Model**
   - In Command Prompt, run:
     ```
     ollama pull hermes3:8b
     ```
   - Confirm it’s downloaded: `ollama list`.

5. **Install Flask**
   - In Command Prompt, run:
     ```
     pip install flask requests
     ```

## Adding the Code
1. **Create Project Folder**
   - Make a folder (e.g., `local-website`) anywhere on your computer.
   - Open it in VS Code: `File > Open Folder`.

2. **Add Files**
   - In VS Code Explorer (Ctrl+Shift+E), create:
     - `app.py`
     - A `templates` folder
     - Inside `templates`, create `index.html`

3. **Copy Code**
   - **app.py**:
     ```python
     from flask import Flask, render_template, request
     import requests

     app = Flask(__name__)

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
                     response_text = response.json().get("response", "No response")
                 except requests.exceptions.RequestException as e:
                     response_text = f"Error: {str(e)}"
         return render_template("index.html", response=response_text, user_input=user_input)

     if __name__ == "__main__":
         app.run(debug=True)
     ```
   - **templates/index.html**:
     ```html
     <!DOCTYPE html>
     <html lang="en">
     <head>
         <meta charset="UTF-8">
         <title>Local Hermes3:8B Website</title>
         <style>
             body { font-family: Arial, sans-serif; margin: 20px; }
             textarea { width: 100%; max-width: 500px; height: 100px; }
             .response { margin-top: 20px; }
         </style>
     </head>
     <body>
         <h1>Ask Hermes3:8B</h1>
         <form method="POST">
             <textarea name="user_input" placeholder="Type your question here...">{{ user_input }}</textarea>
             <br>
             <button type="submit">Submit</button>
         </form>
         <div class="response">
             <h3>Response:</h3>
             <p>{{ response }}</p>
         </div>
     </body>
     </html>
     ```

## Running the Website
1. **Start Ollama**
   - In Command Prompt, run:
     ```
     ollama run hermes3:8b
     ```
   - Keep this terminal open.

2. **Run Flask**
   - In VS Code, open a terminal (Ctrl+``) and navigate to your project folder:
     ```
     cd path\to\local-website
     ```
   - Start the app:
     ```
     python app.py
     ```

3. **Access the Website**
   - Open your browser and go to `http://127.0.0.1:5000`.
   - Type a question in the text box and click "Submit" to see the response.

## Troubleshooting
- **404 Error**: Ensure Ollama is running (`ollama run hermes3:8b`) and the model is listed (`ollama list`).
- **Port Conflict**: If `5000` is busy, edit `app.py` to use `app.run(debug=True, port=5001)`.
- **No Response**: Check Flask terminal for errors and verify Ollama is on `http://localhost:11434`.