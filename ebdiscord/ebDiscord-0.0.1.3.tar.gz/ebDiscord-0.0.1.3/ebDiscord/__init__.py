import asyncio

import discord
from discord import app_commands, Emoji, PartialEmoji
from discord import Interaction as Interaction
from discord.enums import ButtonStyle
from typing import Literal, Optional, Union, Type

temp_eb_buttons = {}
view_list = []


def add_to_temp_ebb_i(custom_id: str, func: callable):
    global temp_eb_buttons
    if custom_id in temp_eb_buttons and temp_eb_buttons[custom_id] != func:
        raise Exception("ebDiscord Error: Custom ID is already in use! or No custom ID was given!")
    temp_eb_buttons[custom_id] = func


class button:
    def __init__(self, func: Optional[callable] = None,
                 label: Optional[str] = None,
                 custom_id: Optional[str] = None,
                 disabled: bool = False,
                 style: ButtonStyle = ButtonStyle.secondary,
                 emoji: Optional[Union[str, Emoji, PartialEmoji]] = None,
                 row: Optional[int] = None):
        self.func = func
        self.label = label
        self.custom_id = custom_id
        self.disabled = disabled
        self.style = style
        self.emoji = emoji
        self.row = row


def new_view(time: Optional[float] = 180.0, components=None):
    if components is None:
        class NewView(discord.ui.View):
            def __init__(self):
                super().__init__(timeout=time)

        return NewView

    class NewView(discord.ui.View):
        def __init__(self):
            super().__init__(timeout=time)

        for component in components:
            add_to_temp_ebb_i(component.custom_id, component.func)
        if len(components) >= 1:
            @discord.ui.button(label=components[0].label, custom_id=components[0].custom_id,
                               disabled=components[0].disabled, style=components[0].style, emoji=components[0].emoji,
                               row=components[0].row)
            async def buttonFunc1(self, interaction: discord.Interaction, dis_button: discord.ui.Button):
                await temp_eb_buttons[dis_button.custom_id](interaction, dis_button)
        if len(components) >= 2:
            @discord.ui.button(label=components[1].label, custom_id=components[1].custom_id,
                               disabled=components[1].disabled, style=components[1].style, emoji=components[1].emoji,
                               row=components[1].row)
            async def buttonFunc2(self, interaction: discord.Interaction, dis_button: discord.ui.Button):
                await temp_eb_buttons[dis_button.custom_id](interaction, dis_button)
        if len(components) >= 3:
            @discord.ui.button(label=components[2].label, custom_id=components[2].custom_id,
                               disabled=components[2].disabled, style=components[2].style, emoji=components[2].emoji,
                               row=components[2].row)
            async def buttonFunc3(self, interaction: discord.Interaction, dis_button: discord.ui.Button):
                await temp_eb_buttons[dis_button.custom_id](interaction, dis_button)
        if len(components) >= 4:
            @discord.ui.button(label=components[3].label, custom_id=components[3].custom_id,
                               disabled=components[3].disabled, style=components[3].style, emoji=components[3].emoji,
                               row=components[3].row)
            async def buttonFunc4(self, interaction: discord.Interaction, dis_button: discord.ui.Button):
                await temp_eb_buttons[dis_button.custom_id](interaction, dis_button)
        if len(components) >= 5:
            @discord.ui.button(label=components[4].label, custom_id=components[4].custom_id,
                               disabled=components[4].disabled, style=components[4].style, emoji=components[4].emoji,
                               row=components[4].row)
            async def buttonFunc5(self, interaction: discord.Interaction, dis_button: discord.ui.Button):
                await temp_eb_buttons[dis_button.custom_id](interaction, dis_button)
        if len(components) >= 6:
            @discord.ui.button(label=components[5].label, custom_id=components[5].custom_id,
                               disabled=components[5].disabled, style=components[5].style, emoji=components[5].emoji,
                               row=components[5].row)
            async def buttonFunc6(self, interaction: discord.Interaction, dis_button: discord.ui.Button):
                await temp_eb_buttons[dis_button.custom_id](interaction, dis_button)
        if len(components) >= 7:
            @discord.ui.button(label=components[6].label, custom_id=components[6].custom_id,
                               disabled=components[6].disabled, style=components[6].style, emoji=components[6].emoji,
                               row=components[6].row)
            async def buttonFunc7(self, interaction: discord.Interaction, dis_button: discord.ui.Button):
                await temp_eb_buttons[dis_button.custom_id](interaction, dis_button)
        if len(components) >= 8:
            @discord.ui.button(label=components[7].label, custom_id=components[7].custom_id,
                               disabled=components[7].disabled, style=components[7].style, emoji=components[7].emoji,
                               row=components[7].row)
            async def buttonFunc8(self, interaction: discord.Interaction, dis_button: discord.ui.Button):
                await temp_eb_buttons[dis_button.custom_id](interaction, dis_button)
        if len(components) >= 9:
            @discord.ui.button(label=components[8].label, custom_id=components[8].custom_id,
                               disabled=components[8].disabled, style=components[8].style, emoji=components[8].emoji,
                               row=components[8].row)
            async def buttonFunc9(self, interaction: discord.Interaction, dis_button: discord.ui.Button):
                await temp_eb_buttons[dis_button.custom_id](interaction, dis_button)
        if len(components) >= 10:
            @discord.ui.button(label=components[9].label, custom_id=components[9].custom_id,
                               disabled=components[9].disabled, style=components[9].style, emoji=components[9].emoji,
                               row=components[9].row)
            async def buttonFunc10(self, interaction: discord.Interaction, dis_button: discord.ui.Button):
                await temp_eb_buttons[dis_button.custom_id](interaction, dis_button)
        if len(components) >= 11:
            @discord.ui.button(label=components[10].label, custom_id=components[10].custom_id,
                               disabled=components[10].disabled, style=components[10].style, emoji=components[10].emoji,
                               row=components[10].row)
            async def buttonFunc11(self, interaction: discord.Interaction, dis_button: discord.ui.Button):
                await temp_eb_buttons[dis_button.custom_id](interaction, dis_button)
        if len(components) >= 12:
            @discord.ui.button(label=components[11].label, custom_id=components[11].custom_id,
                               disabled=components[11].disabled, style=components[11].style, emoji=components[11].emoji,
                               row=components[11].row)
            async def buttonFunc12(self, interaction: discord.Interaction, dis_button: discord.ui.Button):
                await temp_eb_buttons[dis_button.custom_id](interaction, dis_button)
        if len(components) >= 13:
            @discord.ui.button(label=components[12].label, custom_id=components[12].custom_id,
                               disabled=components[12].disabled, style=components[12].style, emoji=components[12].emoji,
                               row=components[12].row)
            async def buttonFunc13(self, interaction: discord.Interaction, dis_button: discord.ui.Button):
                await temp_eb_buttons[dis_button.custom_id](interaction, dis_button)
        if len(components) >= 14:
            @discord.ui.button(label=components[13].label, custom_id=components[13].custom_id,
                               disabled=components[13].disabled, style=components[13].style, emoji=components[13].emoji,
                               row=components[13].row)
            async def buttonFunc14(self, interaction: discord.Interaction, dis_button: discord.ui.Button):
                await temp_eb_buttons[dis_button.custom_id](interaction, dis_button)
        if len(components) >= 15:
            @discord.ui.button(label=components[14].label, custom_id=components[14].custom_id,
                               disabled=components[14].disabled, style=components[14].style, emoji=components[14].emoji,
                               row=components[14].row)
            async def buttonFunc15(self, interaction: discord.Interaction, dis_button: discord.ui.Button):
                await temp_eb_buttons[dis_button.custom_id](interaction, dis_button)
        if len(components) >= 16:
            @discord.ui.button(label=components[15].label, custom_id=components[15].custom_id,
                               disabled=components[15].disabled, style=components[15].style, emoji=components[15].emoji,
                               row=components[15].row)
            async def buttonFunc16(self, interaction: discord.Interaction, dis_button: discord.ui.Button):
                await temp_eb_buttons[dis_button.custom_id](interaction, dis_button)
        if len(components) >= 17:
            @discord.ui.button(label=components[16].label, custom_id=components[16].custom_id,
                               disabled=components[16].disabled, style=components[16].style, emoji=components[16].emoji,
                               row=components[16].row)
            async def buttonFunc17(self, interaction: discord.Interaction, dis_button: discord.ui.Button):
                await temp_eb_buttons[dis_button.custom_id](interaction, dis_button)
        if len(components) >= 18:
            @discord.ui.button(label=components[17].label, custom_id=components[17].custom_id,
                               disabled=components[17].disabled, style=components[17].style, emoji=components[17].emoji,
                               row=components[17].row)
            async def buttonFunc18(self, interaction: discord.Interaction, dis_button: discord.ui.Button):
                await temp_eb_buttons[dis_button.custom_id](interaction, dis_button)
        if len(components) >= 19:
            @discord.ui.button(label=components[18].label, custom_id=components[18].custom_id,
                               disabled=components[18].disabled, style=components[18].style, emoji=components[18].emoji,
                               row=components[18].row)
            async def buttonFunc19(self, interaction: discord.Interaction, dis_button: discord.ui.Button):
                await temp_eb_buttons[dis_button.custom_id](interaction, dis_button)
        if len(components) >= 20:
            @discord.ui.button(label=components[19].label, custom_id=components[19].custom_id,
                               disabled=components[19].disabled, style=components[19].style, emoji=components[19].emoji,
                               row=components[19].row)
            async def buttonFunc20(self, interaction: discord.Interaction, dis_button: discord.ui.Button):
                await temp_eb_buttons[dis_button.custom_id](interaction, dis_button)
        if len(components) >= 21:
            @discord.ui.button(label=components[20].label, custom_id=components[20].custom_id,
                               disabled=components[20].disabled, style=components[20].style, emoji=components[20].emoji,
                               row=components[20].row)
            async def buttonFunc21(self, interaction: discord.Interaction, dis_button: discord.ui.Button):
                await temp_eb_buttons[dis_button.custom_id](interaction, dis_button)
        if len(components) >= 22:
            @discord.ui.button(label=components[21].label, custom_id=components[21].custom_id,
                               disabled=components[21].disabled, style=components[21].style, emoji=components[21].emoji,
                               row=components[21].row)
            async def buttonFunc22(self, interaction: discord.Interaction, dis_button: discord.ui.Button):
                await temp_eb_buttons[dis_button.custom_id](interaction, dis_button)
        if len(components) >= 23:
            @discord.ui.button(label=components[22].label, custom_id=components[22].custom_id,
                               disabled=components[22].disabled, style=components[22].style, emoji=components[22].emoji,
                               row=components[22].row)
            async def buttonFunc23(self, interaction: discord.Interaction, dis_button: discord.ui.Button):
                await temp_eb_buttons[dis_button.custom_id](interaction, dis_button)
        if len(components) >= 24:
            @discord.ui.button(label=components[23].label, custom_id=components[23].custom_id,
                               disabled=components[23].disabled, style=components[23].style, emoji=components[23].emoji,
                               row=components[23].row)
            async def buttonFunc24(self, interaction: discord.Interaction, dis_button: discord.ui.Button):
                await temp_eb_buttons[dis_button.custom_id](interaction, dis_button)
        if len(components) >= 25:
            @discord.ui.button(label=components[24].label, custom_id=components[24].custom_id,
                               disabled=components[24].disabled, style=components[24].style, emoji=components[24].emoji,
                               row=components[24].row)
            async def buttonFunc25(self, interaction: discord.Interaction, dis_button: discord.ui.Button):
                await temp_eb_buttons[dis_button.custom_id](interaction, dis_button)
        if len(components) >= 26:
            raise Exception("Too many buttons")

    return NewView


async def msg(interaction: discord.Interaction, message=None, embed=None, ephemeral: Optional[bool] = False,
              components: Optional[list] = None, component_timeout: Optional[float] = 180.0):
    view = new_view(components=components, time=component_timeout)
    if type(message) == str or type(message) == int:
        if type(embed) == discord.Embed:
            await interaction.response.send_message(str(message), embed=embed, ephemeral=ephemeral, view=view())
        else:
            await interaction.response.send_message(str(message), ephemeral=ephemeral, view=view())
    else:
        if type(message) == discord.Embed:
            if type(embed) == str or type(embed) == int:
                await interaction.response.send_message(str(embed), embed=message, ephemeral=ephemeral, view=view())
            else:
                await interaction.response.send_message(embed=message, ephemeral=ephemeral, view=view())


class settings:
    def __init__(self, token: str, server_id: int, start_message: Optional[str] = None, on_message: Optional[callable] = None):
        self.tree = None
        self.bot = None
        self.user = None
        self.token = token
        self.start_message = start_message
        self.server_id = server_id
        self.server_obj = discord.Object(id=server_id)
        self.view_list_in = view_list
        self.on_message_func = on_message
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
                if global_self.start_message is not None:
                    print(global_self.start_message)


            async def setup_hook(self) -> None:
                for view in global_self.view_list_in:
                    self.add_view(view())

            async def on_message(self, message: discord.Message):
                if global_self.on_message_func is not None:
                    await global_self.on_message_func(message)

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

    def on(self, to_save: Optional[list] = []):
        for buttons in to_save:
            v = new_view(time=None, components=buttons)
            self.view_list_in.append(v)
        self.bot.run(self.token)