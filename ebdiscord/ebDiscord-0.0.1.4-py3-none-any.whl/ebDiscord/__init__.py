import asyncio

import discord
from discord import app_commands, Emoji, PartialEmoji
from discord import Interaction as Interaction
from discord.enums import ButtonStyle
from typing import Literal, Optional, Union, Type, List

temp_eb_components = {}
view_list = []


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


class select:
    def __init__(self, custom_id: Optional[str] = discord.utils.MISSING, placeholder: Optional[str] = None, min_values: int = 1, max_values: int = 1, options: List[discord.SelectOption] = discord.utils.MISSING, disabled: bool = False, row: Optional[int] = None, func: Optional[callable] = None):
        self.custom_id = custom_id
        self.placeholder = placeholder
        self.min_values = min_values
        self.max_values = max_values
        self.options = options
        self.disabled = disabled
        self.row = row
        self.func = func


def add_to_temp_ebb_i(custom_id: str, func: callable, type_component: type):
    global temp_eb_components
    if custom_id in temp_eb_components and temp_eb_components[custom_id] != func:
        raise Exception(f"ebDiscord Error: Custom ID is already in use! or no custom ID was given! id name: {custom_id}")
    temp_eb_components[custom_id] = func


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
            add_to_temp_ebb_i(component.custom_id, component.func, type(component))

        for i in components:
            if i.func == None and i.custom_id != None and not i.disabled:
                print('\033[93m' + f"ebDiscord Waring: No function was entered and the component is not disabled given for id: {i.custom_id}!" + '\033[0m')

        if len(components) >= 1:
            if type(components[0]) == button:
                @discord.ui.button(label=components[0].label, custom_id=components[0].custom_id,
                                   disabled=components[0].disabled, style=components[0].style, emoji=components[0].emoji,
                                   row=components[0].row)
                async def buttonFunc1(self, interaction: discord.Interaction, dis_button: discord.ui.Button):
                    await temp_eb_components[dis_button.custom_id](interaction, dis_button)
            elif type(components[0]) == select:
                @discord.ui.select(custom_id=components[0].custom_id, placeholder=components[0].placeholder,
                                   min_values=components[0].min_values, max_values=components[0].max_values,
                                   options=components[0].options, disabled=components[0].disabled, row=components[0].row)
                async def selectFunc1(self, interaction: discord.Interaction, dis_select: discord.ui.Select):
                    await temp_eb_components[dis_select.custom_id](interaction, dis_select)
        if len(components) >= 2:
            if type(components[1]) == button:
                @discord.ui.button(label=components[1].label, custom_id=components[1].custom_id,
                                   disabled=components[1].disabled, style=components[1].style, emoji=components[1].emoji,
                                   row=components[1].row)
                async def buttonFunc2(self, interaction: discord.Interaction, dis_button: discord.ui.Button):
                    await temp_eb_components[dis_button.custom_id](interaction, dis_button)
            elif type(components[1]) == select:
                @discord.ui.select(custom_id=components[1].custom_id, placeholder=components[1].placeholder,
                                   min_values=components[1].min_values, max_values=components[1].max_values,
                                   options=components[1].options, disabled=components[1].disabled, row=components[1].row)
                async def selectFunc2(self, interaction: discord.Interaction, dis_select: discord.ui.Select):
                    await temp_eb_components[dis_select.custom_id](interaction, dis_select)
        if len(components) >= 3:
            if type(components[2]) == button:
                @discord.ui.button(label=components[2].label, custom_id=components[2].custom_id,
                                   disabled=components[2].disabled, style=components[2].style, emoji=components[2].emoji,
                                   row=components[2].row)
                async def buttonFunc3(self, interaction: discord.Interaction, dis_button: discord.ui.Button):
                    await temp_eb_components[dis_button.custom_id](interaction, dis_button)
            elif type(components[2]) == select:
                @discord.ui.select(custom_id=components[2].custom_id, placeholder=components[2].placeholder,
                                   min_values=components[2].min_values, max_values=components[2].max_values,
                                   options=components[2].options, disabled=components[2].disabled, row=components[2].row)
                async def selectFunc3(self, interaction: discord.Interaction, dis_select: discord.ui.Select):
                    await temp_eb_components[dis_select.custom_id](interaction, dis_select)
        if len(components) >= 4:
            if type(components[3]) == button:
                @discord.ui.button(label=components[3].label, custom_id=components[3].custom_id,
                                   disabled=components[3].disabled, style=components[3].style, emoji=components[3].emoji,
                                   row=components[3].row)
                async def buttonFunc4(self, interaction: discord.Interaction, dis_button: discord.ui.Button):
                    await temp_eb_components[dis_button.custom_id](interaction, dis_button)
            elif type(components[3]) == select:
                @discord.ui.select(custom_id=components[3].custom_id, placeholder=components[3].placeholder,
                                   min_values=components[3].min_values, max_values=components[3].max_values,
                                   options=components[3].options, disabled=components[3].disabled, row=components[3].row)
                async def selectFunc4(self, interaction: discord.Interaction, dis_select: discord.ui.Select):
                    await temp_eb_components[dis_select.custom_id](interaction, dis_select)
        if len(components) >= 5:
            if type(components[4]) == button:
                @discord.ui.button(label=components[4].label, custom_id=components[4].custom_id,
                                   disabled=components[4].disabled, style=components[4].style, emoji=components[4].emoji,
                                   row=components[4].row)
                async def buttonFunc5(self, interaction: discord.Interaction, dis_button: discord.ui.Button):
                    await temp_eb_components[dis_button.custom_id](interaction, dis_button)
            elif type(components[4]) == select:
                @discord.ui.select(custom_id=components[4].custom_id, placeholder=components[4].placeholder,
                                   min_values=components[4].min_values, max_values=components[4].max_values,
                                   options=components[4].options, disabled=components[4].disabled, row=components[4].row)
                async def selectFunc5(self, interaction: discord.Interaction, dis_select: discord.ui.Select):
                    await temp_eb_components[dis_select.custom_id](interaction, dis_select)
        if len(components) >= 6:
            if type(components[5]) == button:
                @discord.ui.button(label=components[5].label, custom_id=components[5].custom_id,
                                   disabled=components[5].disabled, style=components[5].style, emoji=components[5].emoji,
                                   row=components[5].row)
                async def buttonFunc6(self, interaction: discord.Interaction, dis_button: discord.ui.Button):
                    await temp_eb_components[dis_button.custom_id](interaction, dis_button)
            elif type(components[5]) == select:
                @discord.ui.select(custom_id=components[5].custom_id, placeholder=components[5].placeholder,
                                   min_values=components[5].min_values, max_values=components[5].max_values,
                                   options=components[5].options, disabled=components[5].disabled, row=components[5].row)
                async def selectFunc6(self, interaction: discord.Interaction, dis_select: discord.ui.Select):
                    await temp_eb_components[dis_select.custom_id](interaction, dis_select)
        if len(components) >= 7:
            if type(components[6]) == button:
                @discord.ui.button(label=components[6].label, custom_id=components[6].custom_id,
                                   disabled=components[6].disabled, style=components[6].style, emoji=components[6].emoji,
                                   row=components[6].row)
                async def buttonFunc7(self, interaction: discord.Interaction, dis_button: discord.ui.Button):
                    await temp_eb_components[dis_button.custom_id](interaction, dis_button)
            elif type(components[6]) == select:
                @discord.ui.select(custom_id=components[6].custom_id, placeholder=components[6].placeholder,
                                   min_values=components[6].min_values, max_values=components[6].max_values,
                                   options=components[6].options, disabled=components[6].disabled, row=components[6].row)
                async def selectFunc7(self, interaction: discord.Interaction, dis_select: discord.ui.Select):
                    await temp_eb_components[dis_select.custom_id](interaction, dis_select)
        if len(components) >= 8:
            if type(components[7]) == button:
                @discord.ui.button(label=components[7].label, custom_id=components[7].custom_id,
                                   disabled=components[7].disabled, style=components[7].style, emoji=components[7].emoji,
                                   row=components[7].row)
                async def buttonFunc8(self, interaction: discord.Interaction, dis_button: discord.ui.Button):
                    await temp_eb_components[dis_button.custom_id](interaction, dis_button)
            elif type(components[7]) == select:
                @discord.ui.select(custom_id=components[7].custom_id, placeholder=components[7].placeholder,
                                   min_values=components[7].min_values, max_values=components[7].max_values,
                                   options=components[7].options, disabled=components[7].disabled, row=components[7].row)
                async def selectFunc8(self, interaction: discord.Interaction, dis_select: discord.ui.Select):
                    await temp_eb_components[dis_select.custom_id](interaction, dis_select)
        if len(components) >= 9:
            if type(components[8]) == button:
                @discord.ui.button(label=components[8].label, custom_id=components[8].custom_id,
                                   disabled=components[8].disabled, style=components[8].style, emoji=components[8].emoji,
                                   row=components[8].row)
                async def buttonFunc9(self, interaction: discord.Interaction, dis_button: discord.ui.Button):
                    await temp_eb_components[dis_button.custom_id](interaction, dis_button)
            elif type(components[8]) == select:
                @discord.ui.select(custom_id=components[8].custom_id, placeholder=components[8].placeholder,
                                   min_values=components[8].min_values, max_values=components[8].max_values,
                                   options=components[8].options, disabled=components[8].disabled, row=components[8].row)
                async def selectFunc9(self, interaction: discord.Interaction, dis_select: discord.ui.Select):
                    await temp_eb_components[dis_select.custom_id](interaction, dis_select)
        if len(components) >= 10:
            if type(components[9]) == button:
                @discord.ui.button(label=components[9].label, custom_id=components[9].custom_id,
                                   disabled=components[9].disabled, style=components[9].style, emoji=components[9].emoji,
                                   row=components[9].row)
                async def buttonFunc10(self, interaction: discord.Interaction, dis_button: discord.ui.Button):
                    await temp_eb_components[dis_button.custom_id](interaction, dis_button)
            elif type(components[9]) == select:
                @discord.ui.select(custom_id=components[9].custom_id, placeholder=components[9].placeholder,
                                   min_values=components[9].min_values, max_values=components[9].max_values,
                                   options=components[9].options, disabled=components[9].disabled, row=components[9].row)
                async def selectFunc10(self, interaction: discord.Interaction, dis_select: discord.ui.Select):
                    await temp_eb_components[dis_select.custom_id](interaction, dis_select)
        if len(components) >= 11:
            if type(components[10]) == button:
                @discord.ui.button(label=components[10].label, custom_id=components[10].custom_id,
                                   disabled=components[10].disabled, style=components[10].style, emoji=components[10].emoji,
                                   row=components[10].row)
                async def buttonFunc11(self, interaction: discord.Interaction, dis_button: discord.ui.Button):
                    await temp_eb_components[dis_button.custom_id](interaction, dis_button)
            elif type(components[10]) == select:
                @discord.ui.select(custom_id=components[10].custom_id, placeholder=components[10].placeholder,
                                   min_values=components[10].min_values, max_values=components[10].max_values,
                                   options=components[10].options, disabled=components[10].disabled, row=components[10].row)
                async def selectFunc11(self, interaction: discord.Interaction, dis_select: discord.ui.Select):
                    await temp_eb_components[dis_select.custom_id](interaction, dis_select)
        if len(components) >= 12:
            if type(components[11]) == button:
                @discord.ui.button(label=components[11].label, custom_id=components[11].custom_id,
                                   disabled=components[11].disabled, style=components[11].style, emoji=components[11].emoji,
                                   row=components[11].row)
                async def buttonFunc12(self, interaction: discord.Interaction, dis_button: discord.ui.Button):
                    await temp_eb_components[dis_button.custom_id](interaction, dis_button)
            elif type(components[11]) == select:
                @discord.ui.select(custom_id=components[11].custom_id, placeholder=components[11].placeholder,
                                   min_values=components[11].min_values, max_values=components[11].max_values,
                                   options=components[11].options, disabled=components[11].disabled, row=components[11].row)
                async def selectFunc12(self, interaction: discord.Interaction, dis_select: discord.ui.Select):
                    await temp_eb_components[dis_select.custom_id](interaction, dis_select)
        if len(components) >= 13:
            if type(components[12]) == button:
                @discord.ui.button(label=components[12].label, custom_id=components[12].custom_id,
                                   disabled=components[12].disabled, style=components[12].style, emoji=components[12].emoji,
                                   row=components[12].row)
                async def buttonFunc13(self, interaction: discord.Interaction, dis_button: discord.ui.Button):
                    await temp_eb_components[dis_button.custom_id](interaction, dis_button)
            elif type(components[12]) == select:
                @discord.ui.select(custom_id=components[12].custom_id, placeholder=components[12].placeholder,
                                   min_values=components[12].min_values, max_values=components[12].max_values,
                                   options=components[12].options, disabled=components[12].disabled, row=components[12].row)
                async def selectFunc13(self, interaction: discord.Interaction, dis_select: discord.ui.Select):
                    await temp_eb_components[dis_select.custom_id](interaction, dis_select)
        if len(components) >= 14:
            if type(components[13]) == button:
                @discord.ui.button(label=components[13].label, custom_id=components[13].custom_id,
                                   disabled=components[13].disabled, style=components[13].style, emoji=components[13].emoji,
                                   row=components[13].row)
                async def buttonFunc14(self, interaction: discord.Interaction, dis_button: discord.ui.Button):
                    await temp_eb_components[dis_button.custom_id](interaction, dis_button)
            elif type(components[13]) == select:
                @discord.ui.select(custom_id=components[13].custom_id, placeholder=components[13].placeholder,
                                   min_values=components[13].min_values, max_values=components[13].max_values,
                                   options=components[13].options, disabled=components[13].disabled, row=components[13].row)
                async def selectFunc14(self, interaction: discord.Interaction, dis_select: discord.ui.Select):
                    await temp_eb_components[dis_select.custom_id](interaction, dis_select)
        if len(components) >= 15:
            if type(components[14]) == button:
                @discord.ui.button(label=components[14].label, custom_id=components[14].custom_id,
                                   disabled=components[14].disabled, style=components[14].style, emoji=components[14].emoji,
                                   row=components[14].row)
                async def buttonFunc15(self, interaction: discord.Interaction, dis_button: discord.ui.Button):
                    await temp_eb_components[dis_button.custom_id](interaction, dis_button)
            elif type(components[14]) == select:
                @discord.ui.select(custom_id=components[14].custom_id, placeholder=components[14].placeholder,
                                   min_values=components[14].min_values, max_values=components[14].max_values,
                                   options=components[14].options, disabled=components[14].disabled, row=components[14].row)
                async def selectFunc15(self, interaction: discord.Interaction, dis_select: discord.ui.Select):
                    await temp_eb_components[dis_select.custom_id](interaction, dis_select)
        if len(components) >= 16:
            if type(components[15]) == button:
                @discord.ui.button(label=components[15].label, custom_id=components[15].custom_id,
                                   disabled=components[15].disabled, style=components[15].style, emoji=components[15].emoji,
                                   row=components[15].row)
                async def buttonFunc16(self, interaction: discord.Interaction, dis_button: discord.ui.Button):
                    await temp_eb_components[dis_button.custom_id](interaction, dis_button)
            elif type(components[15]) == select:
                @discord.ui.select(custom_id=components[15].custom_id, placeholder=components[15].placeholder,
                                   min_values=components[15].min_values, max_values=components[15].max_values,
                                   options=components[15].options, disabled=components[15].disabled, row=components[15].row)
                async def selectFunc16(self, interaction: discord.Interaction, dis_select: discord.ui.Select):
                    await temp_eb_components[dis_select.custom_id](interaction, dis_select)
        if len(components) >= 17:
            if type(components[16]) == button:
                @discord.ui.button(label=components[16].label, custom_id=components[16].custom_id,
                                   disabled=components[16].disabled, style=components[16].style, emoji=components[16].emoji,
                                   row=components[16].row)
                async def buttonFunc17(self, interaction: discord.Interaction, dis_button: discord.ui.Button):
                    await temp_eb_components[dis_button.custom_id](interaction, dis_button)
            elif type(components[16]) == select:
                @discord.ui.select(custom_id=components[16].custom_id, placeholder=components[16].placeholder,
                                   min_values=components[16].min_values, max_values=components[16].max_values,
                                   options=components[16].options, disabled=components[16].disabled, row=components[16].row)
                async def selectFunc17(self, interaction: discord.Interaction, dis_select: discord.ui.Select):
                    await temp_eb_components[dis_select.custom_id](interaction, dis_select)
        if len(components) >= 18:
            if type(components[17]) == button:
                @discord.ui.button(label=components[17].label, custom_id=components[17].custom_id,
                                   disabled=components[17].disabled, style=components[17].style, emoji=components[17].emoji,
                                   row=components[17].row)
                async def buttonFunc18(self, interaction: discord.Interaction, dis_button: discord.ui.Button):
                    await temp_eb_components[dis_button.custom_id](interaction, dis_button)
            elif type(components[17]) == select:
                @discord.ui.select(custom_id=components[17].custom_id, placeholder=components[17].placeholder,
                                   min_values=components[17].min_values, max_values=components[17].max_values,
                                   options=components[17].options, disabled=components[17].disabled, row=components[17].row)
                async def selectFunc18(self, interaction: discord.Interaction, dis_select: discord.ui.Select):
                    await temp_eb_components[dis_select.custom_id](interaction, dis_select)
        if len(components) >= 19:
            if type(components[18]) == button:
                @discord.ui.button(label=components[18].label, custom_id=components[18].custom_id,
                                   disabled=components[18].disabled, style=components[18].style, emoji=components[18].emoji,
                                   row=components[18].row)
                async def buttonFunc19(self, interaction: discord.Interaction, dis_button: discord.ui.Button):
                    await temp_eb_components[dis_button.custom_id](interaction, dis_button)
            elif type(components[18]) == select:
                @discord.ui.select(custom_id=components[18].custom_id, placeholder=components[18].placeholder,
                                   min_values=components[18].min_values, max_values=components[18].max_values,
                                   options=components[18].options, disabled=components[18].disabled, row=components[18].row)
                async def selectFunc19(self, interaction: discord.Interaction, dis_select: discord.ui.Select):
                    await temp_eb_components[dis_select.custom_id](interaction, dis_select)
        if len(components) >= 20:
            if type(components[19]) == button:
                @discord.ui.button(label=components[19].label, custom_id=components[19].custom_id,
                                   disabled=components[19].disabled, style=components[19].style, emoji=components[19].emoji,
                                   row=components[19].row)
                async def buttonFunc20(self, interaction: discord.Interaction, dis_button: discord.ui.Button):
                    await temp_eb_components[dis_button.custom_id](interaction, dis_button)
            elif type(components[19]) == select:
                @discord.ui.select(custom_id=components[19].custom_id, placeholder=components[19].placeholder,
                                   min_values=components[19].min_values, max_values=components[19].max_values,
                                   options=components[19].options, disabled=components[19].disabled, row=components[19].row)
                async def selectFunc20(self, interaction: discord.Interaction, dis_select: discord.ui.Select):
                    await temp_eb_components[dis_select.custom_id](interaction, dis_select)
        if len(components) >= 21:
            if type(components[20]) == button:
                @discord.ui.button(label=components[20].label, custom_id=components[20].custom_id,
                                   disabled=components[20].disabled, style=components[20].style, emoji=components[20].emoji,
                                   row=components[20].row)
                async def buttonFunc21(self, interaction: discord.Interaction, dis_button: discord.ui.Button):
                    await temp_eb_components[dis_button.custom_id](interaction, dis_button)
            elif type(components[20]) == select:
                @discord.ui.select(custom_id=components[20].custom_id, placeholder=components[20].placeholder,
                                   min_values=components[20].min_values, max_values=components[20].max_values,
                                   options=components[20].options, disabled=components[20].disabled, row=components[20].row)
                async def selectFunc21(self, interaction: discord.Interaction, dis_select: discord.ui.Select):
                    await temp_eb_components[dis_select.custom_id](interaction, dis_select)
        if len(components) >= 22:
            if type(components[21]) == button:
                @discord.ui.button(label=components[21].label, custom_id=components[21].custom_id,
                                   disabled=components[21].disabled, style=components[21].style, emoji=components[21].emoji,
                                   row=components[21].row)
                async def buttonFunc22(self, interaction: discord.Interaction, dis_button: discord.ui.Button):
                    await temp_eb_components[dis_button.custom_id](interaction, dis_button)
            elif type(components[21]) == select:
                @discord.ui.select(custom_id=components[21].custom_id, placeholder=components[21].placeholder,
                                   min_values=components[21].min_values, max_values=components[21].max_values,
                                   options=components[21].options, disabled=components[21].disabled, row=components[21].row)
                async def selectFunc22(self, interaction: discord.Interaction, dis_select: discord.ui.Select):
                    await temp_eb_components[dis_select.custom_id](interaction, dis_select)
        if len(components) >= 23:
            if type(components[22]) == button:
                @discord.ui.button(label=components[22].label, custom_id=components[22].custom_id,
                                   disabled=components[22].disabled, style=components[22].style, emoji=components[22].emoji,
                                   row=components[22].row)
                async def buttonFunc23(self, interaction: discord.Interaction, dis_button: discord.ui.Button):
                    await temp_eb_components[dis_button.custom_id](interaction, dis_button)
            elif type(components[22]) == select:
                @discord.ui.select(custom_id=components[22].custom_id, placeholder=components[22].placeholder,
                                   min_values=components[22].min_values, max_values=components[22].max_values,
                                   options=components[22].options, disabled=components[22].disabled, row=components[22].row)
                async def selectFunc23(self, interaction: discord.Interaction, dis_select: discord.ui.Select):
                    await temp_eb_components[dis_select.custom_id](interaction, dis_select)
        if len(components) >= 24:
            if type(components[23]) == button:
                @discord.ui.button(label=components[23].label, custom_id=components[23].custom_id,
                                   disabled=components[23].disabled, style=components[23].style, emoji=components[23].emoji,
                                   row=components[23].row)
                async def buttonFunc24(self, interaction: discord.Interaction, dis_button: discord.ui.Button):
                    await temp_eb_components[dis_button.custom_id](interaction, dis_button)
            elif type(components[23]) == select:
                @discord.ui.select(custom_id=components[23].custom_id, placeholder=components[23].placeholder,
                                   min_values=components[23].min_values, max_values=components[23].max_values,
                                   options=components[23].options, disabled=components[23].disabled, row=components[23].row)
                async def selectFunc24(self, interaction: discord.Interaction, dis_select: discord.ui.Select):
                    await temp_eb_components[dis_select.custom_id](interaction, dis_select)
        if len(components) >= 25:
            if type(components[24]) == button:
                @discord.ui.button(label=components[24].label, custom_id=components[24].custom_id,
                                   disabled=components[24].disabled, style=components[24].style, emoji=components[24].emoji,
                                   row=components[24].row)
                async def buttonFunc25(self, interaction: discord.Interaction, dis_button: discord.ui.Button):
                    await temp_eb_components[dis_button.custom_id](interaction, dis_button)
            elif type(components[24]) == select:
                @discord.ui.select(custom_id=components[24].custom_id, placeholder=components[24].placeholder,
                                   min_values=components[24].min_values, max_values=components[24].max_values,
                                   options=components[24].options, disabled=components[24].disabled, row=components[24].row)
                async def selectFunc25(self, interaction: discord.Interaction, dis_select: discord.ui.Select):
                    await temp_eb_components[dis_select.custom_id](interaction, dis_select)
        if len(components) >= 26:
            raise Exception("Too many components")

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
    def __init__(self, token: str, server_id: int, start_message: Optional[str] = None,
                 on_message: Optional[callable] = None):
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
