# std
import os
import subprocess
from typing import List, Optional as Opt

# internal
from tier.internal.git.commit import Commit


class Git:

    def __init__(self, dirpath: Opt[str] = None):
        self.dirpath = dirpath or os.getcwd()

    def is_git(self):
        res = self.capture('rev-parse', '--is-inside-work-tree', check=False)
        print(res)

    def commits(self, commit1: str, commit2: str = 'HEAD', path: Opt[str] = None) -> List[Commit]:
        commit_ids = self.commit_ids(commit1, commit2, path)
        return [Commit(commit_id, git=self) for commit_id in commit_ids]

    def commit_ids(self, commit1: str, commit2: str = 'HEAD', path: Opt[str] = None) -> List[str]:
        args = [
            'log',
            f'{commit1}..{commit2}',
            '--pretty=%H',
        ]
        if path:
            args.append(path)
        return self.capture(*args).splitlines()

    def latest_commit_id(self, path: Opt[str] = None) -> str:
        args = ['log', '-n', '1', '--pretty=%H']
        if path:
            args.append(path)
        return self.capture(*args)

    def top_level(self) -> str:
        return self.capture('rev-parse', '--show-toplevel')

    def run(self, *args: str, check: bool = True):
        subprocess.run(
            ['git'] + list(args),
            check=check,
            cwd=self.dirpath,
        )

    def capture(self, *args: str, check: bool = True, strip: bool = True) -> str:
        res = subprocess.run(
            ['git'] + list(args),
            capture_output=True,
            check=check,
            cwd=self.dirpath,
        )
        captured = res.stdout.decode()
        if strip:
            captured = captured.strip()
        return captured
