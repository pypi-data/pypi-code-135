from setuptools import setup, find_packages

setup(
    name='nonebot_plugin_ygo_trade',
    version="1.0.0",
    description=(
        'nonebot的游戏王查价插件'
    ),
    long_description=open('README.md','r',encoding='utf-8').read(),
    long_description_content_type="text/markdown",
    author='kaguya',
    author_email='467241156@qq.com',
    maintainer='kaguya',
    maintainer_email='467241156@qq.com',
    packages=find_packages(),
    platforms=["all"],
    url='https://github.com/Kaguyaya/nonebot_plugin_ygotrade',
    install_requires=[
        'aiohttp',
        'nonebot-adapter-onebot>=2.0.0-beta.1,<3.0.0',
        'nonebot2>=2.0.0-beta.1,<3.0.0',
    ]
)
