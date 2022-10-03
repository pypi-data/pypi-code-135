import discord
from discord import app_commands
from discord import Interaction as Interaction
from typing import Literal


async def msg(interaction: discord.Interaction, message=None, embed=None, ephemeral=False):
    if type(message) == str or type(message) == int:
        if type(embed) == discord.Embed:
            await interaction.response.send_message(str(message), embed=embed, ephemeral=ephemeral)
        else:
            await interaction.response.send_message(str(message), ephemeral=ephemeral)
    else:
        if type(message) == discord.Embed:
            if type(embed) == str or type(embed) == int:
                await interaction.response.send_message(str(embed), embed=message, ephemeral=ephemeral)
            else:
                await interaction.response.send_message(embed=message, ephemeral=ephemeral)


class settings:
    def __init__(self, token: str, server_id: int, start_message=""):
        self.tree = None
        self.bot = None
        self.user = None
        self.token = token
        self.start_message = start_message
        self.server_id = server_id
        self.server_obj = discord.Object(id=server_id)
        self.view_list = []
        self.make_bot()

    def make_bot(self):
        class abot(discord.Client):
            def __init__(self):
                super().__init__(intents=discord.Intents.all())
                self.synced = False

            async def on_ready(self):
                await local_tree.sync(guild=global_self.server_obj)
                global_self.user = self.user
                self.synced = True
                print(global_self.start_message)

            async def setup_hook(self) -> None:
                for view in global_self.view_list:
                    self.add_view(view())

        global_self = self
        local_bot = abot()
        self.bot = local_bot
        self.tree = app_commands.CommandTree(self.bot)

        local_tree = self.tree
        return local_bot

    # TODO options: list = None, guild_id: int = None
    def new_command(self, name: str, command_func: callable, description: str):
        local_tree = self.tree

        @local_tree.command(name=name.lower(), description=description, guild=self.server_obj)
        async def run(interaction: Interaction):
            await command_func(interaction)

    def on(self):
        self.bot.run(self.token)
