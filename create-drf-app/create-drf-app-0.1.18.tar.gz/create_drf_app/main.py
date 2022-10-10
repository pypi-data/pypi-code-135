import os
import platform
import pathlib

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
    current_dir_path = os.path.dirname(script_path)
    templates_path = os.path.join(current_dir_path, "templates")
    return os.path.join(templates_path, template_name)
    

def activate_venv(path):

    # set current directory
    os.chdir(path)
    os.system("python -m venv venv")
    print("🔨 setting up your virutal environment")

    env_activate_script = ""
    if OS == "Windows":
        env_activate_script = "Scripts"

    activate_file = os.path.join(path, "env", env_activate_script, "activate")
    os.system(f"{activate_file} && pip install -r requirements.txt")
    print("✏️ downloading packages")


@app.command("")
def main(template_name):
    template_path = get_template_path(template_name)
    path = cookiecutter(template_path)
    activate_venv(path)
    print("💥 your DRF project is ready!")
    folder_name = pathlib.PurePath(path)
    if OS == "Windows":
        activate_file = os.path.join(path, "env", "Scripts", "activate")
        print(f"cd {folder_name} && {activate_file}")

