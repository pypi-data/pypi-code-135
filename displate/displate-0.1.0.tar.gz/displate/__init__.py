import click
import os

@click.command()
@click.option("--file",help="name of the file to write boilerplate.", required=True)
@click.option("--type",help="type of to write boilerplate.", required=True)
def utility(file,type):
    if file[:-3] != ".py":
        fn = f"{file}.py"
    else:
        fn = file
    if fn in os.listdir():
        if type == "main":
            with open(fn,"w") as f:
                f.write("import discord\nfrom discord.ext import commands\n\nbot = commands.Bot(command_prefix='!',intents=discord.Intents.default())\n\n@bot.listen('on_ready')\nasync def _on_ready():\n\tprint('i am ready')\n\nbot.run('t')")
            click.echo("successfully written main code!")
        elif type == "cogs":
            with open(fn,"w") as f:
                f.write("import discord\nfrom discord.ext import commands\n\nclass name(commands.Cog):\n\tdef __init__(self,bot):\n\t\tself.bot = bot\n\n\t@commands.command()\n\tasync def name(self,ctx):\n\t\tawait ctx.send('hello')\n\nasync def setup(bot):\n\tawait bot.add_cog(name(bot))")
            click.echo("successfully written cogs code!")
        else:
            click.echo("no such type!")
    else:
        click.echo("no such file!")

if __name__ == '__main__':
    utility()

# python main.py --file ts --type cogs
