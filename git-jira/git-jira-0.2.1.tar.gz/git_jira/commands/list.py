import click
from git_jira.jira import JiraProject
from git_jira.git import GitRepo
from git_jira.utils import print_table

columns = ['key', 'type', 'summary', 'branch', 'assignee']

def classify_issues(project_code=None, status=None):
    issues = JiraProject(project_code=project_code).get_issues(status=status)
    branches = GitRepo().get_branches()
    classified_issues = [[issue.key, issue.type, issue.summary, "no branch", issue.assignee] for issue in issues if issue.branch_name not in branches]
    classified_issues.extend([[issue.key, issue.type, issue.summary, issue.branch_name, issue.assignee] for issue in issues if issue.branch_name in branches])
    return classified_issues


@click.command()
@click.option('-s', '--status', help='List issues with this status', default='Planned', type=str)
def list(status):
    click.echo("Getting available issues...")
    issues = classify_issues(status=status)
    click.echo(print_table(columns, issues))
    