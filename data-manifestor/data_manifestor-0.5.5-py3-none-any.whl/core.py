from typing import Any, Dict, Optional, Tuple, Union

import logging
import os
from glob import glob

from np_lims_tk.core import get_project_asset, get_project_name, put_project_asset
from np_lims_tk.local_paths import path_to_lims_meta

from .exceptions import DataManifestorError, ManifestError, PathError
from .models import (
    LocalComparisonResult,
    Manifest,
    Template,
    alt_dict_to_template,
    dict_to_template,
    dump_Template,
    is_alt_format,
)
from .paths import generate_path_pattern, resolve_paths

logger = logging.getLogger(__name__)


def generate_manifest(template_dict: dict[str, Any], *args: str) -> Manifest:
    """Generates a data_manifestor manifest from a template_dict and arguments
    required by the template.
    """
    try:
        if is_alt_format(template_dict):
            template = alt_dict_to_template(template_dict)
        else:
            template = dict_to_template(template_dict)

        path_patterns = [
            generate_path_pattern(template.path_prefix, path_pattern, *args)
            for path_pattern in template.path_patterns
        ]
    except Exception as e:
        raise ManifestError("Error parsing manifest") from e

    return Manifest(
        name=template.name,
        template=template,
        args=args,
        path_patterns=path_patterns,
    )


def compare_manifest_to_local(
    local_dir: str,
    *args: str,
    template_dict: Optional[dict[str, Any]] = None,
) -> LocalComparisonResult:
    """Gets data manifestor template associated with a given project_name

    Args:
        local_dir: The local file directory to search for files.
        args: Arguments to supply to `template_dict` if supplied.
        template_dict: dict representation of a `Template`.

    Raises:
        ManifestError: Invalid template supplied.

    Returns:
        Results of the comparison.

    Notes:
        - If `template_dict` and `args` aren't supplied, they will be
        inferred from the `local_dir` you're running a local comparison on.
    """
    if not template_dict:
        logger.debug("Autogenerating manifest and args")
        template_dict, args = path_to_manifest_template(local_dir)
        if not template_dict:
            raise ManifestError("Couldnt infer template from path. path=%s" % local_dir)

    manifest = generate_manifest(template_dict, *args)
    resolved_paths = []
    found = []
    missing = []
    for path_pattern in manifest.path_patterns:
        pattern, paths = resolve_paths(local_dir, path_pattern)
        if len(paths) > 0:
            found.extend(paths)
        else:
            missing.append(pattern)
        resolved_paths.append(
            (
                pattern,
                paths,
            )
        )
    return LocalComparisonResult(
        local_dir=local_dir,
        manifest=manifest,
        resolved_paths=resolved_paths,
        found=found,
        missing=missing,
    )


def path_to_manifest_template(path: str) -> tuple[Any, tuple[Any, ...]]:
    """Infers associated manifest template from a file or directory path.

    Args:
        path: File or directory path.

    Returns:
        Template and necessary arguments associated with it.

    Raises:
        ManifestError: An unexpected error occurred.
    """
    try:
        lims_meta = path_to_lims_meta(path)
        logger.debug("Resolved lims meta: %s" % lims_meta)
        lims_id = lims_meta._id
        subject_id = lims_meta.subject_id
        date_str = lims_meta.date_str
        project_name = get_project_name(lims_id=lims_id)
        logger.debug("Resolved project name: %s" % project_name)
        template = get_project_data_manifestor_template(project_name)
        return template, (
            lims_id,
            subject_id,
            date_str,
        )
    except Exception as e:
        raise ManifestError("Error parsing manifest") from e


data_manifestor_project_asset_name = "data_manifestor_template"


def get_project_data_manifestor_template(
    project_name: str = "default",
    client: Optional[Any] = None,  # for integration testing, remove later
) -> Any:
    """Gets data manifestor template associated with a given `project_name`.

    Args:
        project_name: `project_name` associated with the template.
        client: `pymongo.MongoClient` instance to query.

    Returns:
        Associated template or `None` if one doesn't exist.
    """
    return get_project_asset(
        project_name,
        data_manifestor_project_asset_name,
        client=client,
    )


def update_project_data_manifestor_template(
    project_name: str,
    _template: Union[Template, dict[str, Any]],
    client: Optional[Any] = None,  # for integration testing, remove later
) -> Any:
    """Gets data manifestor template associated with a given project_name

    Args:
        project_name: `project_name` associated with the template to update.
        _template: Updated template (or dict representation) to associate with `project_name`.
        client: `pymongo.MongoClient` instance to query.

    Raises:
        DataManifestorError: Invalid template supplied.

    Returns:
        Inserted mongodb record.

    Notes:
        - The full template is expected for `_template`.
        - For more about `project_name` please refer to np_lims_tk docs.
    """
    if isinstance(_template, Template):
        template = _template
    elif isinstance(_template, dict):  # TODO: better way to do this?
        template = Template(**_template)
    else:
        raise DataManifestorError("Invalid template=%s" % _template)

    return put_project_asset(
        project_name,
        data_manifestor_project_asset_name,
        dump_Template(template),
        client=client,
    )
