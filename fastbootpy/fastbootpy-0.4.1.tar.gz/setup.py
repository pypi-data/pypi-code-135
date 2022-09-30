# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['fastbootpy']

package_data = \
{'': ['*']}

install_requires = \
['pyusb>=1.2.1,<2.0.0']

setup_kwargs = {
    'name': 'fastbootpy',
    'version': '0.4.1',
    'description': '',
    'long_description': '# Fastbootpy\n\nFastbootpy is based on pyusb and using libusb1 for USB communications.\n\n---\n\n## Installation\n\n### pip\n\n```bash\npoetry add fastbootpy\n```\n\n### poetry\n\n```bash\npoetry add fastbootpy\n```\n\n---\n\n## Supported fastboot commands\n\n- getvar\n- download\n- upload\n- flash\n- erase\n- boot\n- continue\n- reboot\n\n---\n\n## Examples\n\nAll examples of using library you can find in folder examples.\n\nGet and display all fastboot devices which are connected with pc via usb.\n\n```python\nfrom fastbootpy import FastbootManager\n\n\ndef main() -> None:\n    fastboot_devices = FastbootManager.devices()\n    print("fastboot_devices:", fastboot_devices)\n\n\nif __name__ == "__main__":\n    main()\n```\n\nBoot device into regular mode.\n\n```python\nfrom fastbootpy import FastbootDevice\n\n\ndef main() -> None:\n    serial = "emulator-5554"\n    device = FastbootDevice.connect(serial)\n    device.boot()\n\n\nif __name__ == "__main__":\n    main()\n```\n\nGetvar command example.\n\n```python\nfrom fastbootpy import FastbootDevice, FastbootManager\n\n\ndef main() -> None:\n    fastboot_devices = FastbootManager.devices()\n    serial = fastboot_devices[0]\n    device = FastbootDevice.connect(serial)\n    result = device.getvar("all")\n    print("result:", result)\n\n\nif __name__ == "__main__":\n    main()\n\n```\n',
    'author': 'Orekhov Arkady',
    'author_email': 'arckadyor34@google.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/WorkHardes/fastbootpy',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
