from collections import OrderedDict
from typing import Any
from typing import Dict


async def search_raw(
    hub,
    ctx,
    name: str,
    resource_id: str = None,
) -> Dict:
    """
    Fetch a load balancer from AWS. The return will be in the same format as what the boto3 api returns.

    Can't specify names and LoadBalancerArns in the same call. AWS API is failing with following exception.
        ['ClientError: An error occurred (ValidationError) when calling the 'DescribeLoadBalancers operation:
        Load balancer names and load balancer ARNs cannot be specified at the same time']
    Here, resource_id get higher priority in search than name i.e. if both name and resource_id are not None,
        search is done with resource_id than name.

    Args:
        name(Text): The name of the Idem state.
        resource_id(Text, Optional): AWS ELBv2 Load Balancer ARN to identify the resource.

    Returns:
        {"result": True|False, "comment": A message List, "ret": Dict}

    """
    ret = result = dict(comment=[], ret=None, result=True)
    if resource_id:
        ret = await hub.exec.boto3.client.elbv2.describe_load_balancers(
            ctx,
            LoadBalancerArns=[resource_id],
        )
    elif name:
        ret = await hub.exec.boto3.client.elbv2.describe_load_balancers(
            ctx,
            Names=[name],
        )
    result["result"] = ret["result"]
    result["comment"] = list(ret["comment"])
    result["ret"] = ret["ret"]
    return result


async def update(
    hub,
    ctx,
    current_state: Dict[str, Any],
    input_map: Dict[str, Any],
    resource_id: str,
    plan_state: Dict[str, Any],
):
    r"""
    1. Associates the specified security groups with the specified Application Load Balancer. The specified security
       groups override the previously associated security groups. You can't specify a security group for a Network
       Load Balancer or Gateway Load Balancer.
    2. Enables the Availability Zones for the specified public subnets for the specified Application Load Balancer or
       Network Load Balancer. The specified subnets replace the previously enabled subnets.

       When you specify subnets for a Network Load Balancer, you must include all subnets that were enabled previously,
       with their existing configurations, plus any additional subnets.
    3. Modifies the specified attributes of the specified Application Load Balancer, Network Load Balancer, or
       Gateway Load Balancer.If any of the specified attributes can't be modified as requested, the call fails. Any
       existing attributes that you do not modify retain their current values.

    Args:
        current_state: response returned by describe on an AWS ELB load balancer
        input_map: a dictionary with newly passed values of params.
        resource_id: AWS ELB load balancer name.
        plan_state: idem --test state for update on AWS ElasticLoadBalancing Load Balancer.

    Returns:
        {"result": True|False, "comment": ("A tuple",), "ret": None}

    """
    result = dict(comment=[], result=True, ret=[])
    if not ctx.get("test", False):
        if input_map.get("Attributes"):
            attributes_update = (
                await hub.exec.boto3.client.elbv2.modify_load_balancer_attributes(
                    ctx,
                    LoadBalancerArn=resource_id,
                    Attributes=input_map.get("Attributes"),
                )
            )
            if not attributes_update["result"]:
                result["comment"] = list(attributes_update["comment"])
                result["result"] = False
                return result
            result["comment"].append("Modified Attributes.")
            result["ret"].append({"attributes": attributes_update["ret"]["Attributes"]})

        if input_map.get("SecurityGroups"):
            if not current_state.get("security_groups") or set(
                current_state.get("security_groups")
            ) != set(input_map.get("SecurityGroups")):
                update_security_groups = (
                    await hub.exec.boto3.client.elbv2.set_security_groups(
                        ctx,
                        LoadBalancerArn=resource_id,
                        SecurityGroups=input_map.get("SecurityGroups"),
                    )
                )
                if not update_security_groups["result"]:
                    result["comment"] += list(update_security_groups["comment"])
                    result["result"] = False
                    return result
                result["comment"].append("Updated SecurityGroups.")
                result["ret"].append(
                    {
                        "update_security_groups": update_security_groups["ret"][
                            "SecurityGroupIds"
                        ]
                    }
                )

        if input_map.get("Subnets"):
            if not current_state.get("subnets") or set(
                current_state.get("subnets")
            ) != set(input_map.get("Subnets")):
                update_subnets = await hub.exec.boto3.client.elbv2.set_subnets(
                    ctx,
                    LoadBalancerArn=resource_id,
                    Subnets=input_map.get("Subnets"),
                    IpAddressType=input_map.get("IpAddressType")
                    if input_map.get("Type") != "application"
                    else None,
                )
                if not update_subnets["result"]:
                    result["comment"] += list(update_subnets["comment"])
                    result["result"] = False
                    return result
                result["comment"].append("Updated Subnets.")
                result["ret"].append(
                    {"subnets_update": update_subnets["ret"]["AvailabilityZones"]}
                )

        if input_map.get("IpAddressType"):
            if not current_state.get("ip_address_type") or (
                current_state.get("ip_address_type") != input_map.get("IpAddressType")
            ):
                update_ip_address_type = (
                    await hub.exec.boto3.client.elbv2.set_ip_address_type(
                        ctx,
                        LoadBalancerArn=resource_id,
                        IpAddressType=input_map.get("IpAddressType"),
                    )
                )
                if not update_ip_address_type["result"]:
                    result["comment"] += list(update_ip_address_type["comment"])
                    result["result"] = False
                    return result
                result["comment"].append("Updated IpAddressType.")
                result["ret"].append(
                    {"ip_type_update": update_ip_address_type["ret"]["IpAddressType"]}
                )
    else:
        update_params = OrderedDict(
            {
                "name": input_map.get("LoadBalancerName"),
                "subnets": input_map.get("Subnets"),
                "subnet_mappings": input_map.get("SubnetMappings"),
                "security_groups": input_map.get("SecurityGroups"),
                "scheme": input_map.get("Scheme"),
                "tags": input_map.get("Tags"),
                "lb_type": input_map.get("Type"),
                "ip_address_type": input_map.get("IpAddressType"),
                "customer_owned_ipv4_pool": input_map.get("CustomerOwnedIpv4Pool"),
                "attributes": input_map.get("Attributes"),
                "resource_id": resource_id,
            }
        )
        for key, value in update_params.items():
            if value is not None:
                plan_state[key] = value

        result["ret"] = plan_state
    return result
