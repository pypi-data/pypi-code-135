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


def develop():
    log.debug('tier develop')

    tier = Tier()
    tier.develop()
