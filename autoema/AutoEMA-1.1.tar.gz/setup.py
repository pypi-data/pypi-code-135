""" See: https://github.com/leo-beck/AutoEMA """
from setuptools import setup
import pathlib
import io

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="AutoEMA",
    version="1.1",
    description="Automated Experimental Modal Analysis using Bayesian Optimization",
    long_description_content_type='text/markdown',
    long_description= io.open("README.md", encoding="utf-8").read(),
    url="https://github.com/leo-beck/AutoEMA",
    author="Leopold Beck",
    author_email="l.beck@tum.de",
    keywords="EMA, modal, analysis, automated, mechanics, bayes, bayesian, optimization",
    packages=["AutoEMA"],
    python_requires=">=3.7, <4",
    install_requires=['matplotlib>=3.5.3',
                      'numpy>=1.0',
                      'scikit-learn>=1.1.2',
                      'scipy==1.7.2',
                      'bayesian-optimization>=1.2.0',
                      'sdypy-EMA>=0.24'],
)
