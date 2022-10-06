# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['minivirt', 'minivirt.contrib']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=6.0,<7.0', 'boto3>=1.24.87,<2.0.0', 'click>=8.1.3,<9.0.0']

extras_require = \
{'devel': ['poetry>=1.2.1,<2.0.0', 'pytest>=7.1.3,<8.0.0'],
 'githubactions': ['PyGithub>=1.55,<2.0',
                   'pyngrok>=5.1.0,<6.0.0',
                   'waitress>=2.1.2,<3.0.0']}

entry_points = \
{'console_scripts': ['miv = minivirt.cli:cli']}

setup_kwargs = {
    'name': 'minivirt',
    'version': '0.1b1',
    'description': '',
    'long_description': '# Minivirt\n\nVMs should be easy.\n\n[![Discord](https://badgen.net/badge/icon/discord?icon=discord&label)](https://discord.gg/P72AGcEWHZ)\n\n_Minivirt_ is a lightweight [QEMU][] manager that provides a Docker-like user experience. The default image is based on [Alpine Linux](https://alpinelinux.org/), which is tiny and fast: 50MB compressed disk image, boots to SSH in second(s).\n\n[QEMU]: https://www.qemu.org/\n\n## Installation\n\n1. Install QEMU and other dependencies.\n    * MacOS: `brew install qemu socat`\n    * Debian: `apt install qemu-kvm qemu-utils qemu-efi-aarch64 socat`\n    * Alpine: `apk add py3-pip qemu qemu-system-x86_64 qemu-img socat tar`\n\n1. Install _Minivirt_ and run a checkup.\n    ```shell\n    pip3 install minivirt --pre\n    miv doctor\n    ```\n1. Pull an image and start a VM.\n    ```shell\n    miv remote add default https://f003.backblazeb2.com/file/minivirt\n    miv pull default alpine-{arch} alpine  # {arch} is automatically replaced with your architecture.\n    miv run alpine\n    ```\n\nThe `miv run` command will create an ephemeral VM and open an SSH session into it. When you exit the session, the VM is destroyed.\n\n## Persistent VMs\n\nThe images and VMs are stored in `~/.cache/minivirt/`.\n\nCreate a VM with the `create` command:\n```shell\nmiv create alpine myvm\n```\n\nStart the VM with the terminal attached to its serial console:\n```shell\nmiv start myvm\n```\n\nGracefully stop the VM by sending an ACPI poweroff:\n```shell\nmiv stop myvm\n```\n\nDestroy the VM to remove its disk image and other resources:\n```shell\nmiv destroy myvm\n```\n\nInspect the VMs:\n```shell\nmiv ps\nmiv ps -a  # also shows stopped VMs\n```\n\n### Graphics\n\nStart the VM in the background and connect a display to it:\n```shell\nmiv create alpine myvm\nmiv start myvm --daemon --display\n```\n\nLog in as `root`, and run:\n\n```shell\nsetup-xorg-base\napk add xfce4 xfce4-terminal dbus\nstartx\n```\n\nTo make the screen bigger, right-click on the desktop, hover on _Applications_, then _Settings_, and click _Display_. Select another resolution like "1440x900" and click "apply".\n\n## Images\n\n_Minivirt_ maintains a database of images identified by their SHA256 checksum. They may have any number of tags.\n\nShow images in the database:\n\n```shell\n% miv images\n5446f671 1.4G ubuntu-22.04\n84200bbd 115M alpine-3.15\n8ad24d9f 1.4G ubuntu-20.04\nc86a9115 114M alpine alpine-3.16\n```\n\nCommit a VM as an image:\n\n```shell\nmiv commit myvm myimage\n```\n\nSave the image as a TAR archive:\n\n```shell\nmiv save myimage | gzip -1 > ~/myimage.tgz\n```\n\nLater, load the image:\n\n```shell\nzcat ~/myimage.tgz | miv load myimage\n```\n\nTo make sure the images and VMs are consistent, run a database check:\n\n```shell\nmiv fsck\n```\n\nTo remove an image, first untag it. This only removes the tag, not the image itself.\n\n```shell\nmiv untag myimage\n```\n\nThe image is removed during prune:\n\n```shell\nmiv prune\n```\n\n### Image repositories\n\nAdd a remote repository:\n\n```shell\nmiv remote add default https://f003.backblazeb2.com/file/minivirt\n```\n\nPull an image. `{arch}` will be interpolated to the machine architecture.\n\n```shell\nmiv pull default alpine-{arch} alpine\n```\n\nTo host an image repository, you need an S3-compatible object store (e.g. AWS S3, Backblaze B2). Set the following environment variables:\n\n* `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`: authentication credentials.\n* `AWS_ENDPOINT_URL` _(optional)_: if the object store is not hosted on the AWS public cloud, this should point to the appropriate endpoint.\n\nThe bucket name is taken from the last part of the remote\'s URL, e.g. `minivirt` for the default repository.\n\nRun `miv push` to upload an image:\n\n```shell\nmiv push default alpine-3.16 alpine-3.16-aarch64\n```\n\n## Development\n\n1. Create a virtualenv so you don\'t interfere with gobally-installed packages:\n    ```shell\n    python3 -m venv .venv\n    source .venv/bin/activate\n    ```\n\n1. Install the repo in edit mode and development dependencies:\n    ```shell\n    pip3 install -e .\n    pip3 install pytest\n    ```\n\n1. Run the test suite:\n    ```shell\n    pytest\n    pytest --runslow  # if you\'re not in a hurry\n    ```\n\n### Recipes\n\nMinivirt can build images from recipes, which are YAML files, with a syntax inspired by Github Actions workflows. [The _recipes_ directory](recipes/) contains some examples.\n\n```shell\nmiv build recipes/alpine-3.16.yaml --tag alpine-3.16 -v\n```\n\nThe `-v` flag directs the output of the build (serial console or SSH) to stdout.\n\n### Python API\n\n_Minivirt_ is written in Python and offers a straightforward API:\n\n```python\nfrom minivirt.cli import db\n\nalpine = db.get_image(\'alpine\')\nmyvm = VM.create(db, \'myvm\', image=alpine, memory=512)\nwith myvm.run(wait_for_ssh=30):\n    print(myvm.ssh(\'uname -a\', capture=True))\n```\n\n### GitHub Actions self-hosted runners\n\nMinivirt comes with a server that launches GitHub Actions runners when a workflow job is queued. Each runner is ephemeral and runs in its own VM.\n\n1. Install extra dependencies:\n    ```shell\n    pip install -e minivirt[githubactions]\n    ```\n\n1. Build an actions runner image:\n    ```shell\n    miv build recipes/alpine-3.15.yaml --tag alpine-3.15 -v\n    miv build recipes/ci-alpine.yaml --tag ci-alpine -v\n    miv build recipes/githubactions-alpine.yaml --tag githubactions-alpine -v\n    ```\n\n1. Run the server. To interact with the GitHub API, it needs a [GitHub PAT][], and runs `git credentials fill` to retrieve it. It uses [ngrok][] to listen for webhook events; to avoid the ngrok session timing out, set a token in the `NGROK_AUTH_TOKEN` environment variable.\n    ```shell\n    miv -v githubactions serve githubactions-alpine {repo}\n    ```\n\n[GitHub PAT]: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token\n[ngrok]: https://ngrok.com/\n',
    'author': 'Alex Morega',
    'author_email': 'alex@grep.ro',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
