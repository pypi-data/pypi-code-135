from typing import Dict, List, Union

import jinja2

from .model import Module
from .util import jinja_filters

MODULE_TEMPLATE_STR = """
{{module|escape}} package
{{module|euline}}========
{% if subpackages %}
.. Subpackages
.. -----------

.. toctree::
   :maxdepth: 1
{% for subpackage in subpackages %}
   {{subpackage}}
{% endfor %}
{% endif %}
.. automodule:: {{module}}
   :members:
   :undoc-members:
   :show-inheritance:

{% if submodules %}
.. Submodules
.. ----------
{% for submodule in submodules %}
{{submodule|escape     }} module
{{submodule|euline('+')}}+++++++
.. automodule:: {{submodule}}
   :members:
   :undoc-members:
   :show-inheritance:
{% endfor %}
{% endif %}
"""


def prepare_jinja_template(template: str) -> jinja2.Template:
    env = jinja2.Environment()
    env.filters.update(jinja_filters)

    return env.from_string(template)


def prepare_rst_template_content(
    module: Module, module_hierarchy: List[Module]
) -> Dict[str, Union[str, List[str]]]:
    direct_submodules = [
        m for m in module_hierarchy if m.parent_str == module.module_str
    ]
    subpackages = [m.module_str for m in direct_submodules if m.is_package]
    submodules = [m.module_str for m in direct_submodules if not m.is_package]
    return dict(
        module=module.module_str, subpackages=subpackages, submodules=submodules
    )
