import subprocess
import sys
import os

# Create a virtual environment (venv)
venv_folder = "venv"
if not os.path.exists(venv_folder):
    subprocess.run([sys.executable, "-m", "venv", venv_folder])

# Activate the virtual environment (Windows)
if sys.platform == "win32":
    activate_script = os.path.join(venv_folder, "Scripts", "activate")
    subprocess.run([activate_script], shell=True, text=True)

# Activate the virtual environment (Unix/Linux/Mac)
else:
    activate_script = os.path.join(venv_folder, "bin", "activate")
    subprocess.run([f"source {activate_script}"], shell=True, text=True)

# Install libraries from requirements.txt in the virtual environment
subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

# Run the Streamlit application with arguments
streamlit_command = [sys.executable, "-m", "streamlit", "run", "main.py"]

subprocess.run(streamlit_command)
