#
# Copyright 2022-present Linaro Limited
#
# SPDX-License-Identifier: MIT

import os
import subprocess
import json
import logging
import tempfile

from tuxtrigger.request import get_session


LOG = logging.getLogger("tuxtrigger")
TIMEOUT = 60


def tux_console_build(git_repo, git_ref, target_arch, kconfig, toolchain):
    with tempfile.NamedTemporaryFile(suffix=".json") as json_temp:
        build = subprocess.run(
            [
                "tuxsuite",
                "build",
                "--git-repo",
                git_repo,
                "--git-ref",
                git_ref,
                "--target-arch",
                target_arch,
                "--kconfig",
                kconfig,
                "--toolchain",
                toolchain,
                "--json-out",
                json_temp.name,
                "--no-wait",
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        if build.returncode != 0:
            LOG.warning(f"*build stdout {build.stdout}")
            LOG.warning(f"*build stderr {build.stderr}")
            raise Exception(f"*** Tuxsuite not build repo {build.stderr}")

        LOG.debug(build.stdout)

        json_output = json.load(json_temp)
        LOG.debug(f'\t*** Build UID: {json_output["uid"]}')
        return json_output["uid"]


def tux_console_plan(json_data, plan_file, squad_group, squad_project) -> int:
    if json_data is None:
        LOG.warning("\t** Not able to submit plan -> json output is None")
        return 1
    with tempfile.NamedTemporaryFile(suffix=".json") as json_temp:
        plan = subprocess.run(
            [
                "tuxsuite",
                "plan",
                "--git-repo",
                json_data["git_repo"],
                "--git-ref",
                json_data["git_ref"],
                "--name",
                json_data["git_describe"],
                "--no-wait",
                plan_file,
                "--json-out",
                json_temp.name,
            ]
        )
        if plan.returncode != 0:
            LOG.warning(f'\t** Submiting Plan for {json_data["git_describe"]} failed')
            return 1
        LOG.info(f'\t-> Submiting Plan for {json_data["git_describe"]}')
        squad_submit(json_data, squad_group, squad_project, json_temp.name)
        return 0


def build_result(uid):
    if uid is None:
        return None
    build = subprocess.run(
        ["tuxsuite", "build", "get", uid, "--json"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    json_output = json.loads(build.stdout)
    LOG.debug(f"\t ** JSON OUTPUT: {json_output}")
    LOG.info(
        f'\t-> Build {json_output["uid"]} state: {json_output["state"]}, result: {json_output["result"]}, git describe: {json_output["git_describe"]}'
    )
    return json_output


def squad_submit(json_data, squad_group, squad_project, plan_json):
    if squad_group is None or squad_project is None:
        LOG.warn("** SQUAD config is not available! Unable to process **")
        return 1

    squad = subprocess.run(
        [
            "squad-client",
            "submit-tuxsuite",
            "--group",
            squad_group,
            "--project",
            squad_project,
            "--build",
            json_data["git_describe"],
            "--backend",
            "tuxsuite.com",
            "--json",
            plan_json,
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )

    if squad.returncode != 0:
        LOG.warning(f"*build stdout {squad.stdout}")
        LOG.warning(f"*build stderr {squad.stderr}")
        raise Exception(f"*** squad-client not able to pass data {squad.stderr}")

    LOG.debug(squad.stdout)
    LOG.info(f'\t-> Plan submitted to SQUAD git describe: {json_data["git_describe"]}')
    return 0


def squad_metadata_request(squad_project):
    if squad_project is None:
        LOG.debug(f"SQUAD project {squad_project}")
        LOG.warning("** SQUAD Project is not available!")
        return (None, None)

    base_url = os.getenv("SQUAD_HOST")
    session = get_session(retries=10)

    squad_response = session.get(
        url=f"{base_url}/api/projects/?slug={squad_project}",
        timeout=TIMEOUT,
    )
    if squad_response.status_code != 200:
        LOG.warning(
            f"*SQUAD response error - (get project id) {squad_response.status_code}"
        )
        raise Exception(
            f"SQUAD response error - (get project id) {squad_response.status_code}"
        )
    json_output = json.loads(squad_response.content)
    if json_output["count"] == 0:
        LOG.warning(f"*Project {squad_project} is empty or not created in SQUAD")
        return (None, None)
    project_id = json_output["results"][0]["id"]

    build_response = session.get(
        url=f"{base_url}/api/projects/{project_id}/builds/?ordering=-datetime",
        timeout=TIMEOUT,
    )
    if build_response.status_code != 200:
        LOG.warning(
            f"*SQUAD response error - (get latest build) {build_response.status_code}"
        )
        raise Exception(
            f"SQUAD response error - (get latest build) {build_response.status_code}"
        )
    build_json = json.loads(build_response.content)
    lastest_version_url = build_json["results"][0]["metadata"]

    metadata_response = session.get(url=lastest_version_url, timeout=TIMEOUT)
    if metadata_response.status_code != 200:
        LOG.warning(
            f"*SQUAD response error - (get build metadata) {metadata_response.status_code}"
        )
        raise Exception(
            f"SQUAD response error - (get build metadata) {metadata_response.status_code}"
        )
    metadata_json = json.loads(metadata_response.content)
    if "git_sha" not in metadata_json.keys():
        LOG.warning("**git sha not available in SQUAD metadata")
        return (None, None)
    git_sha = metadata_json["git_sha"]
    fingerprint = metadata_json["fingerprint"]
    LOG.debug(f"git sha found - {git_sha}")
    LOG.debug(f"fingerprint found - {fingerprint}")
    return fingerprint, git_sha


def compare_squad_sha(squad_project, current_sha_value) -> bool:
    if squad_project is None:
        LOG.warning("\t** Previous SHA from SQUAD is not available")
        return True
    previous_sha_from_squad = squad_metadata_request(squad_project)[1]
    if previous_sha_from_squad != current_sha_value:
        LOG.info(
            f"\t-> sha: {current_sha_value} vs \
        previous sha {previous_sha_from_squad}"
        )
        return True
    LOG.info(f"\t-> sha: {current_sha_value}")
    LOG.info("\t-> no changes")
    return False
