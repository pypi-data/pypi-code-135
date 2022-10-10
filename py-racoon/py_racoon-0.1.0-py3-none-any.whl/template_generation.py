from cookiecutter.main import cookiecutter


def project_name(safe_repo_name: str) -> str:
    return " ".join(word.capitalize() for word in safe_repo_name.split("-"))


def package_name(safe_repo_name: str) -> str:
    return safe_repo_name.replace("-", "_")


class Context:
    def __init__(  # noqa: WPS211 too-many-arguments
        self,
        name: str,
        email: str,
        url: str,
        full_name: str,
        src_dir: str,
    ) -> None:
        self._name = name
        self._email = email
        self._git_url = url
        self._docker_repo = full_name
        self.repo_name = full_name.split("/")[-1]
        self._project_name = project_name(safe_repo_name=self.repo_name)
        self._package_name = package_name(safe_repo_name=self.repo_name)
        self._src_dir = src_dir

    def dict(self) -> dict[str, str]:
        return {
            "author_email": self._email,
            "author_name": self._name,
            "git_url": self._git_url,
            "package_name": self._package_name,
            "project_name": self._project_name,
            "repo_name": self.repo_name,
            "docker_repo": self._docker_repo,
            "src_dir": self._src_dir,
        }


def generate_template(template_url: str, context: Context) -> None:
    cookiecutter(
        template=template_url,
        extra_context=context.dict(),
        no_input=True,
    )
