"""
Autogenerated state module using `pop-create-idem <https://gitlab.com/saltstack/pop/pop-create-idem>`__

"""
import copy
from typing import Any
from typing import Dict

__contracts__ = ["resource"]

TREQ = {
    "present": {
        "require": [
            "aws.s3.bucket.present",
        ],
    },
}

BUCKET_NOT_EXISTS_ERROR_MESSAGE = "ClientError: An error occurred (404) when calling the HeadBucket operation: Not Found"


async def present(
    hub,
    ctx,
    name: str,
    bucket: str,
    policy: str,
    confirm_remove_self_bucket_access: bool = None,
    expected_bucket_owner: str = None,
    resource_id: str = None,
) -> Dict[str, Any]:
    r"""
    **Autogenerated function**

    Applies an Amazon S3 bucket policy to an Amazon S3 bucket. If you are using an identity other than the root user of
    the Amazon Web Services account that owns the bucket, the calling identity must have the PutBucketPolicy permissions
    on the specified bucket and belong to the bucket owner's account in order to use this operation. If you don't have
    PutBucketPolicy permissions, Amazon S3 returns a 403 Access Denied error. If you have the correct permissions, but
    you're not using an identity that belongs to the bucket owner's account, Amazon S3 returns a 405 Method Not Allowed error.

    Args:
        name(Text): The name of the bucket policy.
        bucket(Text):  The name of the S3 bucket
        resource_id(Text, optional): S3 Bucket policy ID
        policy(Text): The bucket policy as a JSON document.
        confirm_remove_self_bucket_access(boolean, optional): Set this parameter to true to confirm that you want to remove
                                                            your permissions to change this bucket policy in the future.
        expected_bucket_owner(Text, optional): The account ID of the expected bucket owner. If the bucket is owned
                                                by a different account, the request will fail with an HTTP 403 (Access Denied) error.

    Request Syntax:
        [bucket_name]-policy:
          aws.s3.bucket_policy.present:
            - bucket: string
            - policy: string
            - confirm_remove_self_bucket_access: boolean
            - expected_bucket_owner: string

    Returns:
        Dict[str, Any]

    Examples:

        .. code-block:: sls

            my-s3-bucket-bb7bb32e9533-policy:
              aws.s3.bucket_policy.present:
                - bucket: my-s3-bucket-bb7bb32e9533
                - policy: '{"Version":"2012-10-17","Statement":[{"Sid":"PublicReadGetObject","Effect":"Allow","Principal":{"AWS":"arn:aws:iam::418235808912:root"},"Action":"s3:GetObject","Resource":"arn:aws:s3:::thebugbucket3/*"}]}'
                - confirm_remove_self_bucket_access: False
                - expected_bucket_owner: 1239234249


    """
    result = dict(comment=(), name=name, old_state=None, new_state=None, result=True)

    # Check if Policy state name has correct format i.e. [bucket_name]-policy
    if name.split("-policy")[0] != bucket:
        result["comment"] = (
            f"Incorrect aws.s3.bucket_policy name: {name}. Expected name {bucket}-policy",
        )
        result["result"] = False
        return result

    # Check if bucket exists
    ret = await hub.exec.boto3.client.s3.head_bucket(ctx, Bucket=bucket)
    if not ret["result"]:
        if BUCKET_NOT_EXISTS_ERROR_MESSAGE in ret["comment"]:
            result["comment"] = (f"aws.s3.bucket with name: {bucket} does not exist",)
        else:
            result["comment"] = ret["comment"]
        result["result"] = False
        return result

    before = None
    resource_updated = False
    plan_state = None

    # Get current bucket policy for the bucket
    if resource_id:
        before = await hub.exec.boto3.client.s3.get_bucket_policy(
            ctx, Bucket=bucket, ExpectedBucketOwner=expected_bucket_owner
        )
        if before and not before["result"]:
            result["comment"] = (
                f"Failed to get existing Bucket policy '{name}'. Error : "
                + before["comment"]
            )
            result["result"] = before["result"]
            return result

        result[
            "old_state"
        ] = hub.tool.aws.s3.conversion_utils.convert_raw_bucket_policy_to_present(
            raw_resource=before["ret"], bucket=bucket, name=name
        )
        plan_state = copy.deepcopy(result["old_state"])
        result["comment"] = (f"Bucket policy '{name}' already present.",)
        if result["old_state"]["policy"] != policy:
            resource_updated = True
            plan_state["policy"] = policy

    # Handling test scenario seperately
    if ctx.get("test", False):
        if not before:
            result["new_state"] = hub.tool.aws.test_state_utils.generate_test_state(
                enforced_state={},
                desired_state={
                    "name": name,
                    "policy": policy,
                    "bucket": bucket,
                    "resource_id": bucket + "-policy",
                },
            )
            result["comment"] = (f"Would create aws.s3.bucket_policy '{name}'",)
        else:
            result["new_state"] = plan_state
            if resource_updated:
                result["comment"] = (f"Would update aws.s3.bucket_policy '{name}'",)
            else:
                result["comment"] = (f"No change in policy.",)
        return result

    # If policy is not present or if it is updated
    if (not before) or resource_updated:
        ret = await hub.exec.boto3.client.s3.put_bucket_policy(
            ctx,
            Bucket=bucket,
            Policy=policy,
            ConfirmRemoveSelfBucketAccess=confirm_remove_self_bucket_access,
            ExpectedBucketOwner=expected_bucket_owner,
        )
        result["result"] = ret["result"]
        if not result["result"]:
            result["comment"] = ret["comment"]
            return result
        if resource_updated:
            result["comment"] = result["comment"] + (f"Policy updated successfully",)
        else:
            result["comment"] = (f"Bucket policy '{name}' created.",)
        after = await hub.exec.boto3.client.s3.get_bucket_policy(
            ctx, Bucket=bucket, ExpectedBucketOwner=expected_bucket_owner
        )
        result[
            "new_state"
        ] = hub.tool.aws.s3.conversion_utils.convert_raw_bucket_policy_to_present(
            raw_resource=after["ret"], bucket=bucket, name=name
        )
    else:
        result["new_state"] = copy.deepcopy(result["old_state"])
        result["comment"] = result["comment"] + (f"No change in policy.",)
    return result


async def absent(
    hub,
    ctx,
    name: str,
    bucket: str,
    resource_id: str = None,
    expected_bucket_owner: str = None,
) -> Dict[str, Any]:
    r"""
    **Autogenerated function**

    Deletes the policy of specified s3 bucket.

    Args:
        name(Text): The name of the bucket policy.
        bucket(Text):  The name of the S3 bucket
        resource_id(Text, optional): S3 Bucket policy ID. Idem automatically considers this resource being absent if this field is not specified.
        expected_bucket_owner(Text, optional): The account ID of the expected bucket owner. If the bucket is owned by a
                                    different account, the request will fail with an HTTP 403 (Access Denied) error.

    Returns:
        Dict[str, Any]

    Request Syntax:
        [bucket_name]-policy:
          aws.s3.bucket_policy.absent:
            - bucket: string
            - expected_bucket_owner: string

    Examples:

        .. code-block:: sls

            my-s3-bucket-bb7bb32e9533-policy:
              aws.s3.bucket_policy.absent:
                - bucket: my-s3-bucket-bb7bb32e9533
                - expected_bucket_owner: 1239234249
    """

    result = dict(comment=(), old_state=None, new_state=None, name=name, result=True)
    if not resource_id:
        result["comment"] = hub.tool.aws.comment_utils.already_absent_comment(
            resource_type="aws.s3.bucket_policy", name=name
        )
        return result

    if resource_id.split("-policy")[0] != bucket:
        result["comment"] = (f"Incorrect aws.s3.bucket name: '{bucket}'",)
        result["result"] = False
        return result

    # Check if bucket exists.
    ret = await hub.exec.boto3.client.s3.head_bucket(ctx, Bucket=bucket)
    if not ret["result"]:
        if BUCKET_NOT_EXISTS_ERROR_MESSAGE in ret["comment"]:
            result["comment"] = (f"aws.s3.bucket with name: '{bucket}' does not exist",)
        else:
            result["comment"] = ret["comment"]
        result["result"] = False
        return result

    before = await hub.exec.boto3.client.s3.get_bucket_policy(
        ctx, Bucket=bucket, ExpectedBucketOwner=expected_bucket_owner
    )

    if before and before["result"]:
        result[
            "old_state"
        ] = hub.tool.aws.s3.conversion_utils.convert_raw_bucket_policy_to_present(
            raw_resource=before["ret"], bucket=bucket, name=name
        )

        if ctx.get("test", False):
            result["comment"] = (f"Would delete aws.s3.bucket_policy '{name}'",)
            return result

        ret = await hub.exec.boto3.client.s3.delete_bucket_policy(
            ctx, Bucket=bucket, ExpectedBucketOwner=expected_bucket_owner
        )
        result["result"] = ret["result"]
        if not result["result"]:
            result["comment"] = ret["comment"]
            return result
        result["comment"] = (f"Deleted policy '{name}' for bucket '{bucket}'",)
        return result
    else:
        result["comment"] = hub.tool.aws.comment_utils.already_absent_comment(
            resource_type="aws.s3.bucket_policy", name=name
        )
        return result


async def describe(hub, ctx) -> Dict[str, Dict[str, Any]]:
    """
    Obtain S3 bucket policy for each bucket under the given context for any user.

    Returns:
        Dict[str, Any]

    Examples:

        .. code-block:: bash

            $ idem describe aws.s3.bucket_policy
    """
    result = {}
    # To describe the policy of all the buckets, we first need to list all the buckets, then get the
    # policy of each bucket
    ret = await hub.exec.boto3.client.s3.list_buckets(ctx)

    if not ret["result"]:
        hub.log.debug(f"Could not describe S3 buckets {ret['comment']}")
        return {}

    for bucket in ret["ret"]["Buckets"]:
        bucket_name = bucket.get("Name")
        # get policy for each bucket
        bucket_policy = await hub.exec.boto3.client.s3.get_bucket_policy(
            ctx, Bucket=bucket_name
        )
        if bucket_policy["result"]:
            bucket_policy_name = f"{bucket_name}-policy"
            # translate policy to a common format
            policy_translated = (
                hub.tool.aws.s3.conversion_utils.convert_raw_bucket_policy_to_present(
                    raw_resource=bucket_policy["ret"],
                    bucket=bucket_name,
                    name=bucket_policy_name,
                )
            )
            result[bucket_policy_name] = {
                "aws.s3.bucket_policy.present": [policy_translated]
            }
    return result
