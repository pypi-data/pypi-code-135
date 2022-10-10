import click
from git_jira.git import GitBranch
from git_jira.jira import JiraIssue

@click.command()
def status():
    branch = GitBranch()
    issue = JiraIssue(issue_key = branch.issue_key)
    click.echo(f"Issue type: {issue.type}")
    click.echo(f"Summary: {issue.summary}")
    click.echo(f"Assigned to: {issue.assignee}")
    click.echo(f"Status: {issue.status}")
    click.echo(f"See more at {issue.url}")
