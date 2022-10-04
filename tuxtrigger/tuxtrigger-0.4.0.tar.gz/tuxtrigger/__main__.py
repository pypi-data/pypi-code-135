#
# Copyright 2022-present Linaro Limited
#
# SPDX-License-Identifier: MIT

import contextlib
import logging
import sys
import logging.handlers
import time

from tuxtrigger.argparser import setup_parser
from tuxtrigger.builder import (
    build_result,
    compare_squad_sha,
    squad_metadata_request,
    tux_console_build,
    tux_console_plan,
)
from tuxtrigger.yamlload import (
    pre_tux_run,
    yaml_file_read,
    create_repo_list,
    yaml_file_write,
    compare_sha,
    create_squad_project,
    run_lsremote,
)
from tuxtrigger.manifest import (
    git_manifest_download,
    git_repository_fingerprint,
    manifest_changed,
)

LOG = logging.getLogger("tuxtrigger")

build_params = {
    "git_repo": "",
    "git_ref": "",
    "target_arch": "x86_64",
    "toolchain": "gcc-12",
    "kconfig": "tinyconfig",
}


def main() -> int:
    parser = setup_parser()
    options = parser.parse_args()
    plan_path = options.plan.absolute()
    pre_tux_script = None
    if options.pre_submit:
        pre_tux_script = options.pre_submit.absolute()

    log_handler = logging.StreamHandler(sys.stdout)
    log_handler.setFormatter(logging.Formatter("%(message)s"))
    log_file_handler = logging.handlers.WatchedFileHandler(
        (options.log_file).absolute(),
        mode="w",
    )
    LOG.addHandler(log_handler)
    LOG.addHandler(log_file_handler)

    if options.log_level == "debug":
        LOG.setLevel(logging.DEBUG)
    elif options.log_level == "warn":
        LOG.setLevel(logging.WARNING)
    elif options.log_level == "error":
        LOG.setLevel(logging.ERROR)
    else:
        LOG.setLevel(logging.INFO)

    if options.config:
        uid_queue = list()
        output_data = dict()
        squad_config = dict()
        manifest_json = None
        archive_data_file = None
        config_yaml_data = yaml_file_read(options.config)
        repo_list = create_repo_list(config_yaml_data)
        if any(
            "git.kernel.org" in repo["url"] for repo in config_yaml_data["repositories"]
        ):
            manifest_json = git_manifest_download()

        if options.sha_compare == "yaml":
            output_file = (options.output).absolute()
            output_file.parent.mkdir(exist_ok=True)
            with contextlib.suppress(FileNotFoundError):
                archive_data_file = yaml_file_read(output_file)
                previous_fingerprint = archive_data_file

        LOG.info("Checking repositories:")
        for repo in repo_list:
            value_dict = dict()
            repo_name = repo.url_path()
            group_name = repo.squad_group
            fingerprint = ""
            if "git.kernel.org" in repo_name.netloc:
                fingerprint = git_repository_fingerprint(manifest_json, repo_name.path)
            LOG.info(f"* {repo.url}")
            for branch in repo.branches:
                LOG.info(f' * branch: {branch["name"]}')
                repo_changed = False
                build_params["git_repo"] = repo.url
                build_params["git_ref"] = branch["name"]
                value_dict["fingerprint"] = fingerprint
                squad_project = branch.get(
                    "squad_project",
                    create_squad_project(repo.url_path(), branch["name"]),
                )
                if archive_data_file is None:
                    previous_fingerprint = squad_metadata_request(squad_project)[1]

                if (
                    fingerprint == ""
                    or options.submit == "always"
                    or manifest_changed(
                        repo_name.geturl(), fingerprint, previous_fingerprint
                    )
                ):
                    ls_remote_result = run_lsremote(repo.url, branch["name"])
                    value_dict.update(ls_remote_result)

                    if options.sha_compare == "squad":
                        repo_changed = compare_squad_sha(
                            squad_project, ls_remote_result[branch["name"]]["sha"]
                        )

                    elif options.sha_compare == "yaml":
                        repo_changed = compare_sha(
                            repo_name.geturl(),
                            branch["name"],
                            ls_remote_result,
                            archive_data_file,
                        )

                ls_remote_result = run_lsremote(repo.url, branch["name"])

                value_dict.update(ls_remote_result)

                if options.submit == "never":
                    LOG.info("** Builds suspended **")

                elif repo_changed or options.submit == "always":
                    pre_tux_run(
                        pre_tux_script,
                        repo.url,
                        branch["name"],
                        value_dict,
                        archive_data_file,
                    )
                    build_uid = tux_console_build(**build_params)
                    uid_queue.append(build_uid)
                    squad_config[build_uid] = (
                        branch["plan"],
                        group_name,
                        squad_project,
                    )
            output_data[repo_name.geturl()] = value_dict

        LOG.info("** Build Phase Completed **")

        while uid_queue:
            for uid in uid_queue:
                time.sleep(10)
                json_build_output = build_result(uid)
                if json_build_output["git_describe"] is not None:
                    LOG.debug(f"\t*UID: {uid}")
                    LOG.debug(f"\t*Plan file name: {squad_config[uid][0]}")
                    LOG.debug(f"\t*SQUAD group name: {squad_config[uid][1]}")
                    LOG.debug(f"\t*SQUAD project name: {squad_config[uid][2]}")

                    tux_console_plan(
                        json_build_output,
                        plan_path / squad_config[uid][0],
                        squad_config[uid][1],
                        squad_config[uid][2],
                    )
                    uid_queue.remove(uid)
        LOG.info("** Submiting Plans Phase Completed **")
        if options.sha_compare == "yaml":
            yaml_file_write(output_data, output_file)
            LOG.info("** SHA List Updated **")
    else:
        LOG.info("* Please input path to config yaml file!")
        parser.print_usage()

    return 0


def start() -> None:
    if __name__ == "__main__":
        sys.exit(main())


start()
