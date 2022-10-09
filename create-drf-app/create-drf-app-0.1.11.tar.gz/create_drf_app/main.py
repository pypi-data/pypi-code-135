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
    templates_path = os.path.join(module_path, "templates")
    return os.path.join(templates_path, template_name)
    

def activate_venv(path):

    parent = os.getcwd()
    os.system("python -m venv env")

    env_activate_script = ""
    if OS == "Windows":
        env_activate_script = "Scripts"


    activate_file = os.path.join(path, "env", env_activate_script, "activate")
    os.system(f"{activate_file} && pip install -r requirements.txt")


@app.command("")
def main(template_name):
    template_path = get_template_path(template_name)
    cookiecutter(template_path)
    project_path = os.path.join(template_path, template_name)
    activate_venv(project_path)

