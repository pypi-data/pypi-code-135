from dataclasses import dataclass, field
from typing import Dict, List, Optional

from notes_compiler.config import FolderConfig


@dataclass
class MarkdownTreeNode:
    name: str
    parent: Optional["MarkdownTreeNode"] = None
    children: List["MarkdownTreeNode"] = field(default_factory=list)
    content: Dict = field(default_factory=dict)
    folder_config: FolderConfig = field(default_factory=FolderConfig.default)

    def path_from_root(self):
        if self.parent is None:
            return "."
        else:
            return f"{self.parent.path_from_root()}/{self.name}"

    def path_to_root(self):
        if self.parent is None:
            return "."
        else:
            return f"../{self.parent.path_to_root()}"

    def _print_with_depth(self, d: int = 0) -> str:
        str_repr = f"{'├──' if d else ''}{'───' * max(d - 1, 0)}{self.name}\n"
        for child in self.children:
            str_repr += child._print_with_depth(d + 1)
        str_repr += "|  " * d + "└──────\n"
        return str_repr

    def __str__(self) -> str:
        return self._print_with_depth(0)
