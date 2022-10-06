from setuptools import setup

setup(
    name='nonebot-plugin-dialectlist',
    version='1.3.3',
    author='MYXS',
    author_email='1964324406@qq.com',
    url='https://github.com/X-Skirt-X/nonebot_plugin_dialectlist',
    description=u'一个通过数据库统计群友消息量并作为排行榜发出',
    packages=['nonebot_plugin_dialectlist'],
    install_requires=[
        'pygal',
        'cairosvg',
        'nonebot-adapter-onebot',
        'nonebot_plugin_guild_patch',
        'nonebot_plugin_chatrecorder',
        'nonebot-plugin-chatrecorder-guild-patch',
        ],
)