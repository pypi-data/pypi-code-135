from interactions import (
    Extension,
    Permissions,
    Embed,
    EmbedField,
)


class HelpCMD(Extension):
    def __init__(
        self,
        client,
        name,
        description,
        embed_title,
        embed_description,
        embed_color,
        default_member_permissions,
        ephemeral,
    ):
        self.client = client
        self.name = name
        self.description = description
        self.embed_title = embed_title
        self.embed_description = embed_description
        self.embed_color = embed_color
        self.default_member_permissions = default_member_permissions
        self.ephemeral = ephemeral
        self.allCommands = []
        self.embed: Embed = None

        async def _help(ctx):
            if (
                not self.allCommands
                or self.allCommands != self.client._commands
                or self.embed is None
            ):
                self.allCommands = self.client._commands
                extensions = []
                fields = []
                for i in self.client._extensions.values():
                    if isinstance(i, Extension) and not i.__module__.startswith(
                        "interactions.ext."
                    ):
                        extensions.append(i)
                extensions.sort(key=lambda x: x.__module__)
                for ext in extensions:
                    value = ""
                    for command in ext._commands:
                        cmd = self.client._find_command(command[8:])
                        value += f"`{cmd.name}` - {cmd.description}\n"
                    if value != "":
                        fields.append(
                            EmbedField(
                                name=ext.__class__.__name__, value=value, inline=False
                            )
                        )
                self.embed = Embed(
                    title=self.embed_title,
                    description=self.embed_description,
                    fields=fields,
                )
            await ctx.send(embeds=[self.embed], ephemeral=self.ephemeral)

        self.client.command(
            name=self.name,
            description=self.description,
            default_member_permissions=self.default_member_permissions,
        )(_help)


def setup(
    client,
    cmd_name="help",
    cmd_description="Shows help message",
    embed_title="Help",
    embed_description="Here is a list of all commands and extensions",
    embed_color=0x000000,
    default_member_permissions=Permissions.DEFAULT,
    ephemeral=False,
):
    return HelpCMD(
        client,
        cmd_name,
        cmd_description,
        embed_title,
        embed_description,
        embed_color,
        default_member_permissions,
        ephemeral,
    )
