import git
import os


def pull(path: str, url: str):
    """
    Pull from 'origin' remote of the specified git repository - if the repository does not exist locally, clone it.
    """
    if not os.path.exists(path):
        git.Repo.clone_from(url, path, multi_options=['--depth 1'])

    repo = git.Repo(path)
    remote = repo.remote('origin')
    remote.pull()
