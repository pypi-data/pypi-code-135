from dataclasses import asdict, dataclass
from typing import Any, Dict, List, Optional

from sw_service_lib.platform import API, Operation


@dataclass
class Job:
    id: str
    child_jobs: Optional[List]
    remote_job_id: Optional[str]
    slug: Optional[str]
    resource: Optional[str]
    status: Optional[str]
    is_terminal_state: Optional[str]
    remote_status: Optional[str] = None
    job_data_schema: Optional[str] = None
    job_data: Optional[Dict[str, Any]] = None

    def as_dict(self) -> Dict[str, Any]:
        return asdict(self)

    @staticmethod
    def from_dict(res: dict):
        child_jobs: List[Job] = []
        if "childJobs" in res:
            for _, child_job in res["childJobs"]:
                child_jobs.append(Job.from_dict(child_job))

        return Job(
            id=res["id"],
            remote_job_id=res["remoteJobId"],
            slug=res["slug"],
            resource=res["resource"] if "resource" in res else None,
            status=res["status"],
            is_terminal_state=res["isTerminalState"],
            remote_status=res["remoteStatus"],
            job_data_schema=res["jobDataSchema"],
            job_data=res["jobData"],
            child_jobs=child_jobs,
        )


@dataclass
class File:
    id: str
    slug: Optional[str] = None
    label: Optional[str] = None
    file_name: Optional[str] = None
    url: Optional[str] = None

    @classmethod
    def from_dict(cls, d: dict):
        return File(
            id=d["id"],
            slug=d["slug"],
            label=d["label"],
            url=d["url"],
            file_name=d["fileName"],
        )


create_request = Operation(
    query="""
        mutation jobCreate(
            $resource_slug: String!,
            $workspace_member_slug: String!,
            $parent_job_slug: String,
            $remote_job_id: String,
            $status: JobStatus,
            $remote_status: String,
            $job_data_schema: String,
            $job_data: JSON) {
            jobCreate(input: {
                resourceSlug: $resource_slug,
                workspaceMemberSlug: $workspace_member_slug,
                parentJobSlug: $parent_job_slug,
                remoteJobId: $remote_job_id,
                status: $status,
                remoteStatus: $remote_status,
                jobDataSchema: $job_data_schema,
                jobData: $job_data,
            }) {
                job {
                id
                remoteJobId
                slug
                status
                isTerminalState
                remoteStatus
                jobDataSchema
                jobData
                }
            }
        }
        """,
)


def create(
    api: API,
    resource_slug: str,
    workspace_member_slug: str,
    parent_job_slug: Optional[str] = None,
    remote_job_id: Optional[str] = None,
    status: Optional[str] = None,
    remote_status: Optional[str] = None,
    job_data_schema: Optional[str] = None,
    job_data: Optional[str] = None,
) -> Job:
    """Create a job entry

    Parameters
    ----------
    api: API
        provides access to the platform API.
    resource_slug: str
        used as identifier for the resource.
    workspaceMemberSlug: str
        used to map workspace and user.
    parentJobSlug: Optional[str]
        slug of the job which created this job.
    remoteJobId: Optional[str]
        id typically generated as a result of making a request to an external system.
    status: {Optionapstr
        status of the job. Refer to the  platform for possible values.
    remoteStatus: Optional[str]
        status of job that was initiated on an  external (non-Strangeworks) system.
    jobDataSchema: Optional[str]
        link to the json schema describing job output.
    jobData: Optional[str]
        job output.

    Returns
    -------
    : Job
        The ``Job`` object
    """
    platform_result = api.execute(
        op=create_request,
        **locals(),
    )

    return Job.from_dict(platform_result["jobCreate"]["job"])


update_request = Operation(
    query="""
        mutation jobUpdate(
            $resource_slug: String!,
            $job_slug: String!,
            $parent_job_slug: String,
            $remote_job_id: String,
            $status: JobStatus,
            $remote_status: String,
            $job_data_schema: String,
            $job_data: JSON) {
            jobUpdate(input: {
                resourceSlug: $resource_slug,
                jobSlug: $job_slug,
                parentJobSlug: $parent_job_slug,
                remoteJobId: $remote_job_id,
                status: $status,
                remoteStatus: $remote_status,
                jobDataSchema: $job_data_schema,
                jobData: $job_data,
            }) {
                job {
                id
                remoteJobId
                slug
                status
                isTerminalState
                remoteStatus
                jobDataSchema
                jobData
                }
            }
        }
        """,
)


def update(
    api: API,
    resource_slug: str,
    job_slug: str,
    parent_job_slug: Optional[str] = None,
    remote_job_id: Optional[str] = None,
    status: Optional[str] = None,
    remote_status: Optional[str] = None,
    job_data_schema: Optional[str] = None,
    job_data: Optional[str] = None,
) -> Job:
    """Make an update to a job entry.

    Parameters
    ----------
    api: API
        provides access to the platform API.
    resource_slug: str
        used as identifier for the resource.
    jobSlug: str
        identifier used to retrieve the job.
    parentJobSlug: Optional[str]
        slug of the job which created this job.
    remoteJobId: Optional[str]
        id typically generated as a result of making a request to an external system.
    status: {Optionapstr
        status of the job. Refer to the  platform for possible values.
    remoteStatus: Optional[str]
        status of job that was initiated on an  external (non-Strangeworks) system.
    jobDataSchema: Optional[str]
        link to the json schema describing job output.
    jobData: Optional[str]
        job output.

    Returns
    -------
    : Job
        The ``Job`` object
    """
    platform_result = api.execute(
        op=update_request,
        **locals(),
    )
    return Job.from_dict(platform_result["jobUpdate"]["job"])


get_request = Operation(
    query="""
        query job (
            $resource_slug: String!,
            $job_slug: String!) {
            job(
                resourceSlug: $resource_slug,
                jobSlug: $job_slug
            )
            {
                id
                childJobs {
                    id
                }
                remoteJobId
                slug
                status
                isTerminalState
                remoteStatus
                jobDataSchema
                jobData
            }
        }
    """,
)


def get(
    api: API,
    resource_slug: str,
    job_slug: str,
) -> Job:
    """Retrieve job info

    Parameters
    ----------
    api: API
        provides access to the platform API.
    resource_slug: str
        identifier for the resource.
    jobSlug: str
        identifier used to retrieve the job.

    Returns
    -------
    : Job
        The ``Job`` object
    """
    platform_result = api.execute(
        op=get_request,
        **locals(),
    )
    return Job.from_dict(platform_result["job"])
