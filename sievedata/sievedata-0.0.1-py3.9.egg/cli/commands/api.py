import click

@click.command()
@click.option('--command', help='api operation')
@click.option('--tag', help='tag name')
def api(command, tag):
	if command == "init":
		init_command(tag)
	if command == "edit":
		edit_command(tag)
	if command == "push":
		push_command(tag)

def init_command(tag):
	print("api init subcommand")

def edit_command(tag):
	print("api edit subcommand")

def push_comand(tag):
	print("api push subcommand")
