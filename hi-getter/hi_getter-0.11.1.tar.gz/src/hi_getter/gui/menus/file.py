###################################################################################################
#                              MIT Licence (C) 2022 Cubicpath@Github                              #
###################################################################################################
"""File menu implementation."""
from __future__ import annotations

__all__ = (
    'FileContextMenu',
)

import webbrowser
from shutil import rmtree

from PySide6.QtGui import *
from PySide6.QtWidgets import *

from ...constants import *
from ...models import DeferredCallable
from ...utils.gui import init_objects
from ..app import app
from ..app import tr


# noinspection PyArgumentList
class FileContextMenu(QMenu):
    """Context menu that shows actions to manipulate files."""

    def __init__(self, parent) -> None:
        """Create a new :py:class:`FileContextMenu`."""
        super().__init__(parent)

        init_objects({
            (open_explorer := QAction(self)): {
                'text': tr('gui.menus.file.open'),
                'icon': app().get_theme_icon('dialog_open') or app().icon_store['folder'],
                'triggered': DeferredCallable(
                    webbrowser.open, f'file:///{HI_CACHE_PATH}'
                )
            },

            (flush_cache := QAction(self)): {
                'text': tr('gui.menus.file.flush'),
                'icon': app().get_theme_icon('dialog_discard') or self.style().standardIcon(QStyle.SP_DialogDiscardButton),
                'triggered': self.flush_cache
            },

            (import_from := QAction(self)): {
                'text': tr('gui.menus.file.import'),
                'icon': app().icon_store['import'],
                'triggered': self.import_data
            },

            (export_to := QAction(self)): {
                'text': tr('gui.menus.file.export'),
                'icon': app().icon_store['export'],
                'triggered': self.export_data
            }
        })

        section_map = {
            'Files': (open_explorer, flush_cache, import_from, export_to)
        }

        for section, actions in section_map.items():
            self.addSection(section)
            self.addActions(actions)

        flush_cache.setDisabled(not tuple(HI_CACHE_PATH.iterdir()))  # Set disabled if HI_CACHE_PATH directory is empty

        # TODO: Add functionality and enable
        import_from.setDisabled(True)
        export_to.setDisabled(True)

    def flush_cache(self) -> None:
        """Remove all data from cache."""
        do_flush: bool = app().show_dialog(
            'warnings.delete_cache', self,
            QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel,
            QMessageBox.StandardButton.Cancel
        ).role == QMessageBox.AcceptRole

        if do_flush:
            rmtree(HI_CACHE_PATH)
            HI_CACHE_PATH.mkdir()

    def import_data(self) -> None:
        """Import data from..."""
        ...

    def export_data(self) -> None:
        """Export data to..."""
        ...
