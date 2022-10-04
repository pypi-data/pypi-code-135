################################
# Project templater by Pursuit #
################################
import argparse
import os
import shutil
import subprocess
from typing import Sequence

from newproject import PROGRAM_NAME, PROGRAM_VERSION
from newproject.project import Project
from newproject.util import delete
from newproject.template import template_file


def main(args: Sequence[str] = None) -> None:
    aparser = argparse.ArgumentParser()
    aparser.add_argument("template", help="the template used to create the project (either a local folder or a remote Git repository)")
    aparser.add_argument("name", help="The name of the new project")
    aparser.add_argument("output", help="the folder in which to create the project", nargs="?")
    aparser.add_argument("-v", "--version", help="display the program's version", action="version", version=f"{PROGRAM_NAME} {PROGRAM_VERSION} - by Pursuit")

    args = aparser.parse_args(args)
    template = args.template
    name = args.name
    output = args.output

    if output is None:
        output = name

    if os.path.isdir(output) and len(os.listdir(output)) > 0:
        print(f"Error: The provided output directory {output} exists and is not empty")
        exit(1)

    if os.path.isdir(template):
        print("Copying template directory...")
        shutil.copytree(template, output)
    else:
        print("Cloning template Git repository...")
        retcode = subprocess.call(["git", "clone", template, output])
        if retcode != 0:
            print(f"Git clone failed (return code {retcode})")
            exit(2)

    git_dir = os.path.join(output, ".git")
    if os.path.isdir(git_dir):
        delete(git_dir)

    try:
        print(f"Creating project {name}...")
        project = Project(output)
        context = {
            "project_name": name
        }
        files = project.get_template_files()
        for template in files:
            template_file(template, context)
        for source, dest in project.get_template_paths(context).items():
            source_path = os.path.join(output, source)
            dest_path = os.path.join(output, dest)
            shutil.move(source_path, dest_path)

        print("Deleting template manifest...")
        delete(project.manifest_path)
    except Exception as e:
        print(f"Error: {e}")

    print("Creating Git repository...")
    subprocess.call(["git", "init"], cwd=output)
