import pkg_resources
from pip._internal.commands.list import ListCommand
from pip._vendor.packaging.version import Version


class CustomListCommand(ListCommand):
    def get_outdated(self, packages, options):
        return [
            dist
            for dist in self.iter_packages_latest_infos(packages, options)
            if dist.latest_version > Version(str(dist.version))
        ]


def tons_is_outdated():
    tons_dist = pkg_resources.get_distribution("tons")
    tons_dist.canonical_name = "tons"

    list_command = CustomListCommand(name="list", summary="summary")
    options, args = list_command.parse_args([])
    return len(list_command.get_outdated([tons_dist], options)) == 1
