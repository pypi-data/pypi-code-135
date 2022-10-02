# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pycord_cogsbyserver']

package_data = \
{'': ['*']}

install_requires = \
['py-cord>=2.1.3,<3.0.0']

setup_kwargs = {
    'name': 'pycord-cogsbyserver',
    'version': '0.2.0',
    'description': 'An pycord extension that adds cogs that have a different object for each server.',
    'long_description': '# Pycord Cogs by Server\nA simple addon to the pycord library that allows you to make cogs that exist as different objects between different servers. This is better explained by an example, so say you\'re making a simple music bot. Your cog might look something like this without the library...\n```python\nimport discord\nfrom discord.ext import commands\nclass CogThing(commands.Cog):\n    def __init__(self, bot):\n        self.bot = bot\n        self.queues = {}\n        self.volumes = {}\n    \n    @discord.slash_command()\n    async def add_to_queue(self, ctx, *, song_title):\n        if ctx.guild not in self.queues:\n            self.queues[ctx.guild] = []\n        self.queues[ctx.guild].append(song_title)\n        await ctx.respond("Song added")\n    \n    @discord.slash_command()\n    async def change_volume(self, ctx, *, volume: int):\n        self.volumes[ctx.guild] = volume\n        await ctx.respond(f"Volume set to {volume}")\n    \n    async def play_song(self, vc):\n        if vc.guild not in self.queues or len(self.queues[vc.guild])==0:\n            return\n        \n        song = self.queues[vc.guild].pop(0)\n        volume = 100 if vc.guild not in self.volumes else self.volumes[vc.guild]\n        do_some_things_play_some_music(vc, song, volume)\n```\n...but with the library it can look like this!\n```python\nimport discord\nfrom pycord_cogsbyserver import ServerCog\nclass CogThing(ServerCog):\n    def __init__(self, bot):\n        self.bot = bot\n        self.queue = []\n        self.volume = 100\n    \n    @ServerCog.slash_command()\n    async def add_to_queue(self, ctx, *, song_title):\n        self.queue.append(song_title)\n        await ctx.respond("Song added")\n    \n    @ServerCog.slash_command()\n    async def change_volume(self, ctx, *, volume:int):\n        self.volume = volume\n        await ctx.respond(f"Volume set to {volume}")\n    \n    async def play_song(self, vc):\n        if len(self.queue) == 0:\n            return\n        song = self.queue.pop(0)\n        do_some_things_play_some_music(vc, song, self.volume)\n```\nYou can imagine how that would reduce complexity as the bot\'s functionality increases.',
    'author': 'Nathan Strong',
    'author_email': 'nathanstrong777@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/NathanNull/pycord-cogsbyserver',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
