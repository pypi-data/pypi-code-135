import os.path
from typing import List, Dict

import yaml
import glob
from newproject.template import template_string


class Project:
    MANIFEST_NAMES = ["project.yaml", "project.yml"]

    def __init__(self, path):
        self.path = path
        self.manifest_path = None

        for manifest_name in Project.MANIFEST_NAMES:
            manifest_path = os.path.join(path, manifest_name)
            if os.path.isfile(manifest_path):
                self.manifest_path = manifest_path
        if self.manifest_path is None:
            raise Exception(f"No project manifest file found. Please create a file named '{Project.MANIFEST_NAMES[0]}' in the template directory")
        with open(self.manifest_path, "r") as file:
            manifest = yaml.safe_load(file)
            self.template_name = manifest["template_name"]
            self.template_files = manifest["template_files"]
            self.template_paths = manifest["template_paths"]

    def get_template_files(self) -> List[str]:
        files = []
        for template_glob in self.template_files:
            files += glob.glob(os.path.join(self.path, template_glob), recursive=True)
        return files

    def get_template_paths(self, context) -> Dict[str, str]:
        paths = {}
        for source, dest in self.template_paths.items():
            paths[source] = template_string(dest, context)
        return paths
