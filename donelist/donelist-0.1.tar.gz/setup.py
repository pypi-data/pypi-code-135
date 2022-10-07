from setuptools import setup

setup(
    name="donelist",
    version="0.1",
    py_modules=["donelist"],
    install_requires=[
        "requests",
    ],
    entry_points={
        "console_scripts": [
            "donelist = donelist:add_tasks",
        ]
    }
)
