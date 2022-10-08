import os
import platform
from re import L

import typer
from cookiecutter.main import cookiecutter

OS = platform.system()

app = typer.Typer()

@app.callback()
def callback():
    """
    DRF scaffold
    """

def get_template_path(template_name):
    script_path = os.path.abspath(__file__)
    module_path = os.path.dirname(script_path)
    project_path = os.path.dirname(module_path)
    cookiecutters_path = os.path.join(project_path, "templates")
    return os.path.join(cookiecutters_path, template_name)
    

def install_requirements():
    """
    Creates a virtual environment and installs the requirements
    """

    parent = os.getcwd()
    # full_path = os.path.join(parent, name)
    # os.chdir(full_path)
    os.system("python -m venv env")

    env_sub_dir = ""
    source = ""
    if OS == "Windows":
        env_sub_dir = "Scripts"
    else:
        env_sub_dir = "bin"
        source = ". "

    activate_file = os.path.join(parent, "env", env_sub_dir, "activate")
    os.system(f"{source}{activate_file} && pip install -r requirements.txt")

@app.command()
def main():
    cookiecutter("https://github.com/MohammedBajuaifer/drf-starter-templates.git")

    install_requirements()

