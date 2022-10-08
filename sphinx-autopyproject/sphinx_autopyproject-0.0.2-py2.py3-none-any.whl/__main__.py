import os
import sys
from pathlib import Path

from sphinx.application import Sphinx
from sphinx.cmd.build import main
from sphinx.config import Config, ConfigError

from . import load_from_pyproject, search_pyproject

real_config_read = Config.read


def new_config_read(confdir: str, overrides=None, tags=None):
    namespace = dict(tags=tags, __filename__='pyproject.toml')

    try:
        # pylint: disable=protected-access
        namespace.update(real_config_read(confdir, overrides, tags)._raw_config)
    except ConfigError:
        pass

    load_from_pyproject(
        search_pyproject(
            Path(confdir), Path(confdir).parent, os.getcwd(), *Path(confdir).parents
        ),
        target=namespace,
    )

    return Config(namespace, overrides or {})


setattr(Config, 'read', new_config_read)

real_sphinx_init = Sphinx.__init__


def new_sphinx_init(self, srcdir: str, *args, **kwargs):
    if not os.path.exists(srcdir):
        os.mkdir(srcdir)
    real_sphinx_init(self, srcdir, *args, **kwargs)


setattr(Sphinx, '__init__', new_sphinx_init)

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
