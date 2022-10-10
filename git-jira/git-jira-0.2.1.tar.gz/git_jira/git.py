from sh import git
import re

class GitBranch:
    def __init__(self, name=None):
        if name:
            self.name = name
        else:
            self.name = str(git.branch("--show-current"))[:-1] #Find a better way
            self.issue_key = re.match('^[A-Z]{2}-[0-9]*', self.name)[0]

    def create(self):
        git.checkout("-b", self.name)

class GitRepo:
    def __init__(self):
        pass

    def get_branches(self):
        return [b for b in git("--no-pager", "branch", "--all", "--format='%(refname:short)'").stdout.decode().replace("'", "").split('\n') if len(b)>0]
