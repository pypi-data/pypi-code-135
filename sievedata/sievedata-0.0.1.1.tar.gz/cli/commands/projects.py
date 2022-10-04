from typing import Union
import click
import yaml

from sieve.api.constants import PROJECT_LAYERS

COMMAND_TYPES = {
    "list": ['ls', 'list'],
    "job-status": ['job-status', 'job', 'jobs'],
    "delete": ['delete', 'del'],
    "create": ['create'],
    "push": ['push'],
}

@click.group()
def main():
    pass

@main.command()
@click.argument("project_name", type=str)
@click.argument("command", nargs=1)
@click.argument('extra_arg', required=False)
@click.option("--limit", "-l", type=int, default=100)
@click.option("--offset", "-o", type=int, default=0)
@click.option("--workflow", "-wf", type=click.Path(exists=True))
@click.option("--fps", type=int, default=30)
@click.option("--store-data", type=bool, default=True)
@click.option("--source-name", type=str)
@click.option("--source-url", type=str)
@click.option("--source-path", type=click.Path(exists=True))
def main(
    project_name,
    command,
    extra_arg,
    limit,
    offset,
    workflow,
    fps,
    store_data,
    source_name,
    source_url,
    source_path,
):
    from sieve.api.client import SieveClient, SieveProject
    from sieve.types.api import SieveWorkflow
    client = SieveClient()
    if command in COMMAND_TYPES["list"]:
        for j in client.list_jobs(project_name, limit=limit, offset=offset):
            print(j)
    elif command in COMMAND_TYPES["job-status"]:
        try:
            print(client.get_job(project_name, extra_arg))
        except Exception as e:
            print(str(e))
    elif command in COMMAND_TYPES["delete"]:
        try:
            print(client.delete_project(project_name))
        except Exception as e:
            print(str(e))
    elif command in COMMAND_TYPES["create"]:
        wf = yaml.safe_load(open(workflow, 'r'))
        proj = SieveProject(
            name=project_name,
            workflow=SieveWorkflow.from_json(wf[PROJECT_LAYERS]),
            fps=fps,
            store_data=store_data
        )
        try:
            print(client.create_project(proj))
        except Exception as e:
            print(str(e))
    elif command in COMMAND_TYPES["push"]:
        if source_url:
            local_upload = False
        elif source_path:
            local_upload = True
            source_url = source_path
        try:
            print(client.push(project_name, source_name, source_url, local_upload=local_upload))
        except Exception as e:
            print(str(e))
