from importlib import metadata

import pluggy

from . import pm, settings

__all__ = ["hookimpl"]

hookimpl = pluggy.HookimplMarker(__name__)


def version() -> str:
    return metadata.version(__name__)


def plugin_manager(s: settings.Settings) -> pm.PluginManager:
    return pm.PluginManager.get(s)
