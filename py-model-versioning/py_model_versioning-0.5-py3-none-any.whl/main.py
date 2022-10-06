import click

from py_model_versioning.classes.func import func


@click.group()
def cli():
    pass


@cli.command('print_ver', help="display ver for project")
def print_ver():
    click.echo("0.5")


@cli.command('del_ver', help="delete ver for project")
@click.option('-p', required=True, help="specify project name")
@click.option('-v', required=True, help="specify version name")
def del_ver(p, v):
    call = func()
    call.delete_entire_directory(p + "/" + v + "/")


@cli.command('del_file', help="delete specific file from storage")
@click.option('-f', required=True, help="specify file name to delete")
@click.option('-p', required=True, help="specify project name")
@click.option('-v', required=True, help="specify version name")
def del_file(f, p, v):
    call = func()
    call.delete_file(p + "/" + v + "/", f)


@cli.command('get_file', help="get specific fie from storage")
@click.option('-f', required=True, help="specify file name to get")
@click.option('-p', required=True, help="specify project name")
@click.option('-v', required=True, help="specify version name")
def get_file(f, p, v):
    call = func()
    call.download_file_from_storage(p + "/" + v + "/" + f, f)


@cli.command('get_ver', help="get complete version files for specific project")
@click.option('-p', required=True, help="specify project name")
@click.option('-v', required=True, help="specify version name or all for all versions")
def get_ver(p, v):
    call = func()
    if v != "all":
        call.download_ver_from_storage(p, v)
    else:
        call.download_all_ver_from_storage(p)


@cli.command('init', help="configure cloud provider bucket name and project for google, should be done from root directory")
@click.option('-c', required=True, help="specify cloud provider google or aws currently support only google")
@click.option('-b', required=True, help="specify bucket name")
def init(c, b):
    call = func(False)
    if c.lower() != "google" and c.lower() != "aws":
        click.echo("cloud provider can be google or aws")
    else:
        call.save_config_file(c, b)

@cli.command('init_cloud', help="config")
@click.option('-c', required=True, help="specify cloud provider google or aws currently support only google")
def init_cloud(c):
    call = func(False)
    if c.lower() != "google" and c.lower() != "aws":
        click.echo("cloud provider can be google or aws")
    else:
        call.save_cloud_provider_to_config_file(c)


@cli.command('display_init', help="display the content of configuration file")
def display_init():
    call = func(False)
    call.display_config_file()


@cli.command('ls', help="list storage content, no argument list projects")
@click.option('-p', required=False, help="list all project versions")
@click.option('-v', required=False, help="accomapny with -p list version content")
def ls(p, v):
    call = func()
    if p == None and v == None:
        call.list_dir('', False)
    elif p != None and v == None:
        call.list_dir(p + "/", False)
    else:
        call.list_dir(p + "/" + v, True)


@cli.command('add_directory', help="add directory files to project model version storage")
@click.option('-d', required=True, help="specify directory name to add")
@click.option('-p', required=True, help="specify project name")
@click.option('-v', required=True, help="specify version name")
def add_directory(d, p, v):
    call = func()
    call.add_directory(d, p, v)


@cli.command('add_file', help="add files to project model version storage")
@click.option('-f', required=True, help="specify file name to add or /. to add all files within the folder")
@click.option('-p', required=True, help="specify project name")
@click.option('-v', required=True, help="specify version name")
def add_file(f, p, v):
    call = func()
    call.add_file(p, v, f)


if __name__ == "__main__":
    cli()
