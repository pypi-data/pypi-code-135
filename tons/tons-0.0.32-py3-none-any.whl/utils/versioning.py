from pip._internal.commands.list import ListCommand
from pip._vendor.packaging.version import Version

from tons.version import __version__


class CustomListCommand(ListCommand):
    def get_outdated_by_name(self, canonical_name, cur_version, options):
        cur_version = Version(cur_version)
        with self._build_session(options) as session:
            finder = self._build_package_finder(options, session)

            all_candidates = finder.find_all_candidates(canonical_name)
            if not options.pre:
                all_candidates = [
                    candidate
                    for candidate in all_candidates
                    if not candidate.version.is_prerelease
                ]

            evaluator = finder.make_candidate_evaluator(
                project_name=canonical_name,
            )
            best_candidate = evaluator.sort_best_candidate(all_candidates)
            if best_candidate is None:
                return None

            remote_version = best_candidate.version
            return remote_version > cur_version


def tons_is_outdated():
    list_command = CustomListCommand(name="list", summary="summary")
    options, args = list_command.parse_args([])
    return list_command.get_outdated_by_name("tons", __version__, options)
