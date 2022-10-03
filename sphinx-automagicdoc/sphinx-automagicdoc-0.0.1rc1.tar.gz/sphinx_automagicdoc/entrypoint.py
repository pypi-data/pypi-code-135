# pylint: disable=import-error

from pathlib import Path

from sphinx.application import Sphinx
from sphinx.config import Config
from sphinx.util.logging import getLogger

from . import mock_filesystem
from .mock_filesystem import virtual_files
from .module_scanner import get_module_hierarchy
from .rst_preparation import (
    MODULE_TEMPLATE_STR,
    prepare_jinja_template,
    prepare_rst_template_content,
)

log = getLogger(__name__)


def process_text(data: str) -> str:
    return data


def config_intialized(app: Sphinx, config: Config):
    mock_filesystem.base_path = app.srcdir

    template = prepare_jinja_template(config.automagic_module_template)

    for module_to_process in config.automagic_modules:
        modules = list(
            get_module_hierarchy(module_to_process, ignore=config.automagic_ignore)
        )

        for module in modules:
            if not module.is_package:
                continue

            values = prepare_rst_template_content(module, modules)
            virtual_files[f"{module.module_str}.rst"] = template.render(**values)

    virtual_files.update(
        {
            file_name: process_text(data)
            for file_name, data in config.automagic_files.items()
        }
    )

    virtual_files.update(
        {
            file_name: Path(source_file_name).read_text(encoding='utf-8')
            for file_name, source_file_name in config.automagic_copy_files.items()
        }
    )

    log.info("virtual_files.keys() = %r", list(virtual_files.keys()))
    log.debug("virtual_files = %r", virtual_files)


def setup(app: Sphinx):
    app.connect('config-inited', config_intialized)
    app.add_config_value(
        name='automagic_module_template',
        default=MODULE_TEMPLATE_STR,
        rebuild='env',
        types=[str],
    )

    app.add_config_value(
        name='automagic_modules', default=[], rebuild='env', types=[list]
    )
    app.add_config_value(
        name='automagic_ignore', default=[], rebuild='env', types=[list]
    )
    app.add_config_value(
        name='automagic_files', default={}, rebuild='env', types=[dict]
    )
    app.add_config_value(
        name='automagic_copy_files', default={}, rebuild='env', types=[dict]
    )
