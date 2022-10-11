# std
from typing import Optional as Opt

# internal
from tier.internal.errors import TierException
from tier.internal.git.commit import Commit
from tier.internal.git import git
from tier.internal.git.git import Git
from tier.internal.logging import log
from tier.internal.pyproject import PyProject
from tier.internal.tier import Tier


def init(
        recursive: bool,
        commit: bool,
        tag: bool,
):
    log.debug('tier init')

    if tag:
        commit = True

    log.debug(f'{recursive = }')
    log.debug(f'{commit = }')
    log.debug(f'{tag = }')

    if recursive:
        tier = Tier()
        tier.initialize(commit=commit, tag=tag)
    else:
        project = PyProject()
        Tier.initialize_project(project=project, commit=commit, tag=tag)
