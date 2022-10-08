import os
import re

import gitlab
import pytest

from gitlab_auto_mr.cli import cli


@pytest.mark.parametrize(
    "branch_name, extra_args, expected_title",
    [
        ("feature/test1", {}, "WIP: feature/test1"),
        ("feature-test1", {"-t": "branch2", "-c": "ABC"}, "ABC: feature-test1"),
        ("feature/#1", {"-s": "", "-i": ""}, "WIP: feature/#1"),
        ("feature/v1", {"-d": "tests/data/MR.md"}, "WIP: feature/v1"),
    ],
)
def test_success(runner, branch_name, extra_args, expected_title):
    project_id = 17422070
    gitlab_url = "https://gitlab.com/"
    private_token = os.environ["GITLAB_PRIVATE_TOKEN"]

    args = [
        "--private-token",
        private_token,
        "--source-branch",
        branch_name,
        "--gitlab-url",
        gitlab_url,
        "--project-id",
        project_id,
        "--user-id",
        2902137,
    ]
    [args.extend([k, v]) for k, v in extra_args.items()]
    args = filter(None, args)

    try:
        gitlab_url = re.search("^https?://[^/]+", gitlab_url).group(0)
        gl = gitlab.Gitlab(gitlab_url, private_token=private_token)
        project = gl.projects.get(project_id)
        project.branches.create({"branch": branch_name, "ref": "master"})
        result = runner.invoke(cli, args)
        assert result.exit_code == 0
        mr = project.mergerequests.list()[0]
        target_branch = extra_args["-t"] if "-t" in extra_args else "master"
        check_mr_created_correctly(mr, expected_title, target_branch, branch_name, extra_args)
    finally:
        project.branches.delete(branch_name)
        mr.delete()


def check_mr_created_correctly(mr, expected_title, target_branch, source_branch, extra_args):
    assert mr.attributes["title"] == expected_title
    assert mr.attributes["target_branch"] == target_branch
    assert mr.attributes["source_branch"] == source_branch

    if "-s" in extra_args:
        assert mr.attributes["squash"] == True

    if "-r" in extra_args:
        assert mr.attributes["force_remove_source_branch"] == True

    if "-d" in extra_args:
        assert mr.attributes["description"] == open(extra_args["-d"]).read()

    if "-i" in extra_args:
        assert mr.attributes["labels"] == ["bug", "confirmed", "critical"]
