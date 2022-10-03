from setuptools import setup, find_packages

setup(
        name='web_graph_testing',
        version='0.0.1',
        packages=find_packages(),
        url='https://github.com/NeuroPyPy/web_graph_testing',
        license='MIT',
        author='Flynn OConnell',
        author_email='oconnell@binghamton.edu',
        description='Testing some web/graphical applications and interfaces.',
        install_requires=['flask', 'plotly']
)
