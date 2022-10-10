
from setuptools import setup, find_packages

setup(
    name='qstock',
    version='1.1.0',
    keywords=['pip','qstock'],
    description='Python quantitative finance and stock analysis',
    long_description='金融量化投研平台，更多干货请关注微信公众号：Python金融量化',
    license = "MIT Licence",
    
    url='https://github.com/tkfy920/qstock',
    author='Jinyi Zhang',
    author_email='723195276@qq.com',
    
    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    install_requires = ["numpy", "pandas","matplotlib","pyecharts","tqdm","jieba","seaborn","plotly_express"]
)
