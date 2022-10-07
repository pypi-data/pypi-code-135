# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['admin_action_tools', 'admin_action_tools.templatetags']

package_data = \
{'': ['*'],
 'admin_action_tools': ['static/admin/css/*',
                        'templates/admin/*',
                        'tests/*',
                        'tests/integration/*',
                        'tests/snapshot/*',
                        'tests/unit/*']}

install_requires = \
['Django>=3.2,<=4.2']

setup_kwargs = {
    'name': 'django-admin-action-tools',
    'version': '1.0.0',
    'description': 'Tools for django admin',
    'long_description': '# Django Admin Confirm\n\n[![PyPI](https://img.shields.io/pypi/v/django-admin-action-tools?color=blue)](https://pypi.org/project/django-admin-action-tools/)\n![Tests Status](https://github.com/SpikeeLabs/django-admin-action-tools/actions/workflows/.github/workflows/test.yml/badge.svg)\n[![codecov](https://codecov.io/gh/SpikeeLabs/django-admin-action-tools/branch/main/graph/badge.svg?token=NK5V6YMWW0)](https://codecov.io/gh/SpikeeLabs/django-admin-action-tools)\n![PyPI - Python Version](https://img.shields.io/pypi/pyversions/django-admin-action-tools)\n![PyPI - Django Version](https://img.shields.io/pypi/djversions/django-admin-action-tools)\n![PyPI - License](https://img.shields.io/pypi/l/django_admin_action_tools)\n\n## Features\n- [ ] AdminConfirmMixin\n    Based on [django-admin-confirm](https://github.com/TrangPham/django-admin-confirm) with support for [django-object-actions](https://github.com/crccheck/django-object-actions)\n    AdminConfirmMixin is a mixin for ModelAdmin to add confirmations to change, add and actions.\n- [ ] AdminFormMixin\n    AdminFormMixin is a mixin for ModelAdmin to add a form to configure your actions.\n\n\n## ScreenShot\n![Screenshot of Change Confirmation Page](https://raw.githubusercontent.com/SpikeeLabs/django-admin-action-tools/alpha/docs/images/screenshot.png)\n\n![Screenshot of Add Confirmation Page](https://raw.githubusercontent.com/SpikeeLabs/django-admin-action-tools/alpha/docs/images/screenshot_confirm_add.png)\n\n![Screenshot of Action Confirmation Page](https://raw.githubusercontent.com/SpikeeLabs/django-admin-action-tools/alpha/docs/images/screenshot_confirm_action.png)\n\n\n## Installation\n\nInstall django-admin-action-tools by running:\n\n    poetry add django-admin-action-tools\n\nAdd to INSTALLED_APPS in your project settings before `django.contrib.admin`:\n\n    INSTALLED_APPS = [\n        ...\n        \'admin_action_tools\',\n\n        \'django.contrib.admin\',\n        ...\n    ]\n\nNote that this project follows the template override rules of Django.\nTo override a template, your app should be listed before `admin_confirm`, `admin_form` in INSTALLED_APPS.\n\n## Configuration Options\n\n**Environment Variables**:\n\nCaching is used to cache files for confirmation. When change/add is submitted on the ModelAdmin, if confirmation is required, files will be cached until all validations pass and confirmation is received.\n\n- `ADMIN_CONFIRM_CACHE_TIMEOUT` _default: 1000_\n- `ADMIN_CONFIRM_CACHE_KEY_PREFIX` _default: admin_confirm\\_\\_file_cache_\n\n**Attributes:**\n\n- `confirm_change` _Optional[bool]_ - decides if changes should trigger confirmation\n- `confirm_add` _Optional[bool]_ - decides if additions should trigger confirmation\n- `confirmation_fields` _Optional[Array[string]]_ - sets which fields should trigger confirmation for add/change. For adding new instances, the field would only trigger a confirmation if it\'s set to a value that\'s not its default.\n- `change_confirmation_template` _Optional[string]_ - path to custom html template to use for change/add\n- `action_confirmation_template` _Optional[string]_ - path to custom html template to use for actions\n\nNote that setting `confirmation_fields` without setting `confirm_change` or `confirm_add` would not trigger confirmation for change/add. Confirmations for actions does not use the `confirmation_fields` option.\n\n**Method Overrides:**\nIf you want even more control over the confirmation, these methods can be overridden:\n\n- `get_confirmation_fields(self, request: HttpRequest, obj: Optional[Object]) -> List[str]`\n- `render_change_confirmation(self, request: HttpRequest, context: dict) -> TemplateResponse`\n- `render_action_confirmation(self, request: HttpRequest, context: dict) -> TemplateResponse`\n\n## Usage\n\n### AdminConfirmMixin\nIt can be configured to add a confirmation page on ModelAdmin upon:\n\n- saving changes\n- adding new instances\n- performing actions\n\n**Confirm Change:**\n\n```py\n    from admin_confirm import AdminConfirmMixin\n\n    class MyModelAdmin(AdminConfirmMixin, ModelAdmin):\n        confirm_change = True\n        confirmation_fields = [\'field1\', \'field2\']\n```\n\nThis would confirm changes on changes that include modifications on`field1` and/or `field2`.\n\n**Confirm Add:**\n\n```py\n    from admin_confirm import AdminConfirmMixin\n\n    class MyModelAdmin(AdminConfirmMixin, ModelAdmin):\n        confirm_add = True\n        confirmation_fields = [\'field1\', \'field2\']\n```\n\nThis would confirm add on adds that set `field1` and/or `field2` to a non default value.\n\nNote: `confirmation_fields` apply to both add/change confirmations.\n\n**Confirm Action:**\n\n```py\n    from admin_confirm import AdminConfirmMixin\n\n    class MyModelAdmin(AdminConfirmMixin, ModelAdmin):\n        actions = ["action1", "action2"]\n\n        def action1(modeladmin, request, queryset):\n            # Do something with the queryset\n\n        @confirm_action\n        def action2(modeladmin, request, queryset):\n            # Do something with the queryset\n\n        action2.allowed_permissions = (\'change\',)\n```\n\nThis would confirm `action2` but not `action1`.\n\nAction confirmation will respect `allowed_permissions` and the `has_xxx_permission` methods.\n\n> Note: AdminConfirmMixin does not confirm any changes on inlines\n\n### AdminFormMixin\nTODO\n\n\n## Development\nCheck out our [development process](docs/development_process.md) if you\'re interested.\n',
    'author': 'Thu Trang Pham',
    'author_email': 'thuutrangpham@gmail.com',
    'maintainer': 'jeanloup.monnier',
    'maintainer_email': 'jean-loup.monnier@spikeelabs.fr',
    'url': 'https://github.com/SpikeeLabs/django-admin-action-tools',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
