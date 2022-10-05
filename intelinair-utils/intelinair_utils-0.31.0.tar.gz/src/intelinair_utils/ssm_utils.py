import boto3


def get_ssm_parameter(ssm_client: boto3.client, parameter_name: str) -> str:
    """Returns the value of a SSM parameter.

    Args:
        ssm_client (boto3.client): boto3 ssm client
        parameter_name (str): parameter to get from ssm store

    Returns:
        str: paramenter value
    """
    parameter = ssm_client.get_parameter(Name=parameter_name, WithDecryption=True)
    content = parameter['Parameter']['Value']
    return content
