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
     python app.py or app_new.py
     ```

3. **Access the Website**
   - Open your browser and go to `http://127.0.0.1:5000`.
   - Type a question in the text box and click "Submit" to see the response.

## Running with Docker
1. **Install Docker**
   - Download and install Docker Desktop from [docker.com](https://www.docker.com/products/docker-desktop/).
   - Verify: Run `docker --version` in a terminal.

2. **Build the Docker Image**
   - Navigate to your project folder:
     ```
     cd path\to\local-website
     ```
   - Build the image:
     ```
     docker build -t local-hermes3-website .
     ```

3. **Run the Container**
   - Start the container:
     ```
     docker run -p 5000:5000 -p 11434:11434 local-hermes3-website
     ```
   - Access the website at `http://localhost:5000` in your browser.

## Troubleshooting
- **404 Error**: Ensure Ollama is running (`ollama run hermes3:8b`) and the model is listed (`ollama list`).
- **Port Conflict**: If `5000` is busy, edit `app.py` to use `app.run(debug=True, port=5001)` or adjust Docker port mapping (e.g., `-p 5001:5000`).
- **No Response**: Check Flask terminal for errors and verify Ollama is on `http://localhost:11434`.
- **Docker Issues**: Ensure internet access during `docker build` and sufficient disk space (~5 GB).