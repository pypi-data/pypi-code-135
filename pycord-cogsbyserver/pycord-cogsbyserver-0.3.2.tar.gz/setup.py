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
    'version': '0.3.2',
    'description': 'A pycord extension that adds cogs that have a different object for each server.',
    'long_description': '# Pycord Cogs by Server\nA simple addon to the pycord library that allows you to make cogs that exist as different objects between different servers. This is better explained by an example, so say you\'re making a simple music bot. Your cog might look something like this without the library...\n```python\nimport discord\nfrom discord.ext import commands\nclass CogThing(commands.Cog):\n    def __init__(self, bot):\n        self.bot = bot\n        self.queues = {}\n        self.volumes = {}\n    \n    @discord.slash_command()\n    async def add_to_queue(self, ctx, *, song_title):\n        if ctx.guild not in self.queues:\n            self.queues[ctx.guild] = []\n        self.queues[ctx.guild].append(song_title)\n        await ctx.respond("Song added")\n    \n    @discord.slash_command()\n    async def change_volume(self, ctx, *, volume: int):\n        self.volumes[ctx.guild] = volume\n        await ctx.respond(f"Volume set to {volume}")\n    \n    async def play_song(self, vc):\n        if vc.guild not in self.queues or len(self.queues[vc.guild])==0:\n            return\n        \n        song = self.queues[vc.guild].pop(0)\n        volume = 100 if vc.guild not in self.volumes else self.volumes[vc.guild]\n        do_some_things_play_some_music(vc, song, volume)\n```\n...but with the library it can look like this!\n```python\nimport discord\nfrom pycord_cogsbyserver import ServerCog\nclass CogThing(ServerCog):\n    def __init__(self, bot):\n        self.bot = bot\n        self.queue = []\n        self.volume = 100\n    \n    @ServerCog.slash_command()\n    async def add_to_queue(self, ctx, *, song_title):\n        self.queue.append(song_title)\n        await ctx.respond("Song added")\n    \n    @ServerCog.slash_command()\n    async def change_volume(self, ctx, *, volume:int):\n        self.volume = volume\n        await ctx.respond(f"Volume set to {volume}")\n    \n    async def play_song(self, vc):\n        if len(self.queue) == 0:\n            return\n        song = self.queue.pop(0)\n        do_some_things_play_some_music(vc, song, self.volume)\n```\nYou can imagine how that would reduce complexity as the bot\'s functionality increases.\n\nThe library supports event listeners too, like so:\n```python\nclass CogThing(ServerCog):\n    @ServerCog.listener()\n    async def on_message(self, message):\n        await message.channel.send("infinite loop time")\n```\nThose are sorted by guild as well, or into the special DMs instance if there\'s no one guild that makes sense. In the special case of on_ready, the event instead fires in all cogs, to allow general prep.\n\n## Release Notes/Changelog\nNot a whole lot to say, really. I\'ve done what I\'ve done.\n### V0.3.1\nMINOR SPELLING ERROR (changed summary from "An pycord..." to "A pycord...")\n### V0.3.0\nAdded documentation to literally everything relevant, and a lot of pretty irrelevant things too.\n### V0.2.0\nAdded basic slash command support\n### V0.1.0\nFirst version, ayyyyy! Added basic library functionality in listeners.',
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
