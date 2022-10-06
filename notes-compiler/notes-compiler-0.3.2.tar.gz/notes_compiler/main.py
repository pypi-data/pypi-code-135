import argparse
from subprocess import PIPE, Popen
from typing import Optional
from pathlib import Path
from notes_compiler import VERSION
import os
import os.path
import shutil
import logging
import importlib.resources
from notes_compiler.config import FolderConfig, ProjectConfig
from notes_compiler.html_page import HtmlPage

from notes_compiler.tree_node import MarkdownTreeNode
from notes_compiler.utils import (
    find_file_upwards,
    setup_logging,
    snake_case_to_title_case,
)


class MarkdownTreeProcessor:
    def __init__(self, project_config: ProjectConfig):
        self.project_config = project_config
        self.src_root = (
            project_config.src_root
            if os.path.isabs(project_config.src_root)
            else f"{project_config.root}/{project_config.src_root}"
        )
        self.public_root = (
            project_config.public_root
            if os.path.isabs(project_config.public_root)
            else f"{project_config.root}/{project_config.public_root}"
        )
        self._process()

    def _process(self):
        logging.info("Reading tree...")
        self.tree = self._read_tree(self.src_root)
        logging.info("Reading markdown files...")
        self._read_markdown(self.tree)
        logging.info("Finding files to copy...")
        self._read_files_to_copy(self.tree)
        self._add_builtin_files_to_copy(self.tree)
        logging.info("Building HTML pages...")
        self._make_pages(self.tree)
        logging.info("Processing links...")
        self._decorate_pages(self.tree)

    def output(self):
        self._sync_directories(self.tree)
        self._write_html_tree(self.tree)
        self._write_copy_tree(self.tree)

    def _read_tree(
        self, root_path: str, parent: Optional[MarkdownTreeNode] = None, name: str = ""
    ) -> MarkdownTreeNode:
        config_path = f"{root_path}/notes-folderrc.json"
        if os.path.isfile(config_path):
            config = FolderConfig.from_json_file(config_path)
        else:
            config = FolderConfig.default()
        tree = MarkdownTreeNode(name=name, parent=parent, folder_config=config)
        for entry in os.scandir(root_path):
            if entry.is_dir():
                tree.children.append(
                    self._read_tree(entry.path, name=entry.name, parent=tree)
                )
        return tree

    def _read_markdown(self, tree: MarkdownTreeNode):
        """
        . -> md
        """
        tree.content["markdown"] = []
        for entry in os.scandir(f"{self.src_root}/{tree.path_from_root()}"):
            if entry.is_file() and entry.name.endswith(".md"):
                stem = Path(entry.path).stem
                with open(entry.path, "r") as file:
                    tree.content["markdown"].append(
                        {
                            "name": stem,
                            "content": file.read(),
                            "filename": entry.name,
                        }
                    )
        for child in tree.children:
            self._read_markdown(child)

    def _read_files_to_copy(self, tree: MarkdownTreeNode):
        """
        . -> pages
        """
        tree.content["copy"] = []

        for entry in os.scandir(f"{self.src_root}/{tree.path_from_root()}"):
            if entry.is_file() and not entry.name.endswith(".md"):
                tree.content["copy"].append(
                    {"path": entry.path, "filename": entry.name}
                )
        for child in tree.children:
            self._read_files_to_copy(child)

    def _add_builtin_files_to_copy(self, tree: MarkdownTreeNode):
        # Pygmentize
        pygmentize_cmd = Popen(
            ["pygmentize", "-S", "default", "-f", "html", "-a", ".highlight"],
            stdout=PIPE,
        )
        out, _ = pygmentize_cmd.communicate()
        tree.content["copy"].append(
            {"content": out.decode("utf-8"), "filename": "pygments.css"}
        )
        for traversable in importlib.resources.files(
            "notes_compiler.resources"
        ).iterdir():
            if str(traversable).endswith(".css"):
                with importlib.resources.as_file(traversable) as path:
                    tree.content["copy"].append(
                        {"path": path, "filename": os.path.basename(path)}
                    )

    def _make_pages(self, tree: MarkdownTreeNode):
        """
        md -> pages
        """
        logging.info(f"Building pages at {tree.path_from_root()}")
        tree.content["pages"] = []
        for md in tree.content["markdown"]:
            tree.content["pages"].append(
                {
                    "name": md["name"],
                    "md_filename": md["filename"],
                    "html_filename": md["name"] + ".html",
                    "page": HtmlPage.from_markdown(
                        md=md["content"],
                        name=md["name"],
                        css=self.project_config.css,
                        scripts=self.project_config.scripts,
                        parent=tree,
                    ),
                }
            )
        key = lambda page: page["name"]
        tree.content["pages"] = sorted(tree.content["pages"], key=key)
        for child in tree.children:
            self._make_pages(child)

    def _decorate_pages(self, tree: MarkdownTreeNode):
        """
        pages -> pages
        """
        if tree.folder_config.build_index:
            tree.content["index"] = {
                "name": "index",
                "html_filename": "index.html",
                "page": HtmlPage(
                    body=self._toc(tree),
                    name="index",
                    css=self.project_config.css,
                    parent=tree,
                ),
            }
        else:
            tree.content["index"] = None
        for i, page in enumerate(tree.content["pages"]):
            if i > 0:
                page["page"].page_before = tree.content["pages"][i - 1]["page"]
            if i < len(tree.content["pages"]) - 1:
                page["page"].page_after = tree.content["pages"][i + 1]["page"]
        for child in tree.children:
            self._decorate_pages(child)

    def _sync_directories(self, tree: MarkdownTreeNode):
        full_path = f"{self.public_root}/{tree.path_from_root()}"
        if not os.path.exists(full_path):
            os.makedirs(full_path)
        for child in tree.children:
            self._sync_directories(child)

    def _write_html_tree(self, tree: MarkdownTreeNode):
        """
        pages -> .
        """
        for child in tree.children:
            self._write_html_tree(child)

        if tree.folder_config.build_index:
            with open(
                f"{self.public_root}/{tree.path_from_root()}/{tree.content['index']['html_filename']}",
                "w",
            ) as f:
                f.write(tree.content["index"]["page"].build_page())
        for page in tree.content["pages"]:
            with open(
                f"{self.public_root}/{tree.path_from_root()}/{page['html_filename']}",
                "w",
            ) as f:
                f.write(page["page"].build_page())

    def _write_copy_tree(self, tree: MarkdownTreeNode):
        """
        copy -> .
        """
        for child in tree.children:
            self._write_copy_tree(child)
        for copy in tree.content["copy"]:
            full_path = f"{self.public_root}/{tree.path_from_root()}/{copy['filename']}"
            if "content" in copy:
                with open(full_path, "w") as f:
                    f.write(copy["content"])
            else:
                shutil.copyfile(
                    copy["path"],
                    f"{self.public_root}/{tree.path_from_root()}/{copy['filename']}",
                )

    def _toc(self, tree: MarkdownTreeNode) -> str:
        """
        pages -> .
        """

        def make_toc(tree: MarkdownTreeNode, root: MarkdownTreeNode) -> str:
            toc_str = "<ul>\n"
            for child in tree.children:
                if child.folder_config.build_index:
                    path_to_index = (
                        f"{tree.path_to_root()}/{child.path_from_root()}/index.html"
                    )
                    toc_str += f'<li><a href="{path_to_index}">🗁 {snake_case_to_title_case(child.name)}</a>\n{make_toc(child, root)}</li>'
                else:
                    toc_str += f'<details><summary class="toc-summary">{snake_case_to_title_case(child.name)}</summary>\n{make_toc(child, root)}</details>'
            for page in tree.content["pages"]:
                toc_str += f'<li><a href="{root.path_to_root()}/{tree.path_from_root()}/{page["html_filename"]}">{snake_case_to_title_case(page["name"])}</a></li>\n'
            toc_str += "</ul>"
            return toc_str

        toc_str = (
            f"<h1>{snake_case_to_title_case(tree.name) if tree.name else 'Table of Contents'}</h1>\n"
            + make_toc(tree, tree)
        )

        return toc_str


def main():
    setup_logging()
    parser = argparse.ArgumentParser(prog="notes-compiler")
    parser.add_argument("path", type=str, default=".", nargs="?")
    parser.add_argument(
        "-V", "--version", action="version", version=f"%(prog)s {VERSION}"
    )
    args = parser.parse_args()

    json_config_path = find_file_upwards("notes-projectrc.json", args.path)
    if json_config_path is not None:
        logging.info(f"Loading configuration from JSON file: {json_config_path}")
        config = ProjectConfig.from_json_file(json_config_path)
    else:
        raise Exception(
            "No notes-projectrc.json file found in target directory nor any of its parents."
        )

    tree_processor = MarkdownTreeProcessor(project_config=config)
    tree_processor.output()
