from setuptools import setup

name = "types-pywin32"
description = "Typing stubs for pywin32"
long_description = '''
## Typing stubs for pywin32

This is a PEP 561 type stub package for the `pywin32` package.
It can be used by type-checking tools like mypy, PyCharm, pytype etc. to check code
that uses `pywin32`. The source for this package can be found at
https://github.com/python/typeshed/tree/master/stubs/pywin32. All fixes for
types and metadata should be contributed there.

See https://github.com/python/typeshed/blob/master/README.md for more details.
This package was generated from typeshed commit `27e9fde673d33d1f0bfcf0e14c38f4d31300379f`.
'''.lstrip()

setup(name=name,
      version="304.0.0.0",
      description=description,
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/python/typeshed",
      project_urls={
          "GitHub": "https://github.com/python/typeshed",
          "Changes": "https://github.com/typeshed-internal/stub_uploader/blob/main/data/changelogs/pywin32.md",
          "Issue tracker": "https://github.com/python/typeshed/issues",
          "Chat": "https://gitter.im/python/typing",
      },
      install_requires=[],
      packages=['pythonwin-stubs', 'pythoncom-stubs', 'win32-stubs', 'win32comext-stubs', '_win32typing-stubs'],
      package_data={'pythonwin-stubs': ['__init__.pyi', 'dde.pyi', 'win32ui.pyi', 'win32uiole.pyi', 'METADATA.toml'], 'pythoncom-stubs': ['__init__.pyi', 'METADATA.toml'], 'win32-stubs': ['__init__.pyi', 'lib/__init__.pyi', 'lib/ntsecuritycon.pyi', 'lib/pywintypes.pyi', 'lib/sspicon.pyi', 'lib/win2kras.pyi', 'lib/win32con.pyi', 'lib/win32cryptcon.pyi', 'lib/win32inetcon.pyi', 'lib/win32netcon.pyi', 'lib/winioctlcon.pyi', 'mmapfile.pyi', 'odbc.pyi', 'perfmon.pyi', 'servicemanager.pyi', 'timer.pyi', 'win32api.pyi', 'win32clipboard.pyi', 'win32console.pyi', 'win32cred.pyi', 'win32crypt.pyi', 'win32event.pyi', 'win32evtlog.pyi', 'win32file.pyi', 'win32gui.pyi', 'win32help.pyi', 'win32inet.pyi', 'win32job.pyi', 'win32lz.pyi', 'win32net.pyi', 'win32pdh.pyi', 'win32pipe.pyi', 'win32print.pyi', 'win32process.pyi', 'win32profile.pyi', 'win32ras.pyi', 'win32security.pyi', 'win32service.pyi', 'win32trace.pyi', 'win32transaction.pyi', 'win32ts.pyi', 'win32wnet.pyi', 'wincerapi.pyi', 'winxpgui.pyi', 'winxptheme.pyi', 'METADATA.toml'], 'win32comext-stubs': ['__init__.pyi', 'adsi/__init__.pyi', 'adsi/adsi.pyi', 'authorization/__init__.pyi', 'authorization/authorization.pyi', 'axcontrol/__init__.pyi', 'axcontrol/axcontrol.pyi', 'axdebug/__init__.pyi', 'axdebug/axdebug.pyi', 'axscript/__init__.pyi', 'axscript/axscript.pyi', 'bits/__init__.pyi', 'bits/bits.pyi', 'directsound/__init__.pyi', 'directsound/directsound.pyi', 'ifilter/__init__.pyi', 'ifilter/ifilter.pyi', 'internet/__init__.pyi', 'internet/internet.pyi', 'mapi/__init__.pyi', 'mapi/exchange.pyi', 'mapi/exchdapi.pyi', 'mapi/mapi.pyi', 'propsys/__init__.pyi', 'propsys/propsys.pyi', 'shell/__init__.pyi', 'shell/shell.pyi', 'taskscheduler/__init__.pyi', 'taskscheduler/taskscheduler.pyi', 'METADATA.toml'], '_win32typing-stubs': ['__init__.pyi', 'METADATA.toml']},
      license="Apache-2.0 license",
      classifiers=[
          "License :: OSI Approved :: Apache Software License",
          "Programming Language :: Python :: 3",
          "Typing :: Stubs Only",
      ]
)
