# ollama-gradio-chatbot

Step 1: Download Ollama
Visit the Ollama Website: Go to the Ollama website.
Choose Your Model: Select the model of your choice (e.g., LLaMA 3.2).
Download the Model: Follow the instructions to download the model package.
Step 2: Open Command Prompt
Open Command Prompt: Press Windows + R, type cmd, and hit Enter.
Check Ollama Installation: Run the following command to verify the installation:
bash
ollama info
This command will provide you with details about the installed models.
Step 3: Activate Conda Environment
Open Anaconda Prompt: Find Anaconda Prompt in your start menu and open it.
Activate Your Environment: Use the command to activate your Conda environment:
bash
conda activate <your_env_name>
Replace <your_env_name> with the name of your environment.
Step 4: Verify Model in Jupyter Notebook
Open Jupyter Notebook: Launch Jupyter Notebook from your activated Conda environment by running:
bash
jupyter notebook
Create a New Notebook: Create a new Python notebook and run the following code to test the model:
python
import ollama

response = ollama.generate(model='llama3.2:1b', prompt='Hello')
print(response['response'])
Check Output: Ensure that you receive a valid response from the model.
Step 5: Open VS Code for UI with Gradio
Launch VS Code: Open Visual Studio Code.
Create a New Python File: Create a new file (e.g., llama_chatbot.py) and write the following code in file ...

Step 6: Install Gradio (if not already installed)
Open Terminal in VS Code: Open a terminal within VS Code (View > Terminal).
Install Gradio: Run the following command to install Gradio:
bash
pip install gradio
Step 7: Run Your Gradio App
Run Your Script: In the VS Code terminal, execute your script:
bash
python llama_chatbot.py

Access the Web Interface: A Gradio interface will launch in your web browser where you can interact with the LLaMA model.
