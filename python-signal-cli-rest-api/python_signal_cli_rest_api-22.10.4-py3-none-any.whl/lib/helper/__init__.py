"""
helpers
"""

from base64 import b64decode
from io import BytesIO
from mimetypes import guess_extension
from re import search as re_search
from re import sub as re_sub
from tempfile import mkstemp

from jmespath import search as j_search
from magic import from_buffer
from sanic.log import logger

from python_signal_cli_rest_api.lib.jsonrpc import jsonrpc


def validate_recipients(recipients: list, number: str, version: int = 2):
    """
    Validate recipients. Recipient must be either a phone number
    registered with signal network or a known group id.

    Args:
        recipients (list)
        number (str)
        version (int): API request version

    Returns:
        tuple: tuple of lists ``(unknown: list, contacts: list, groups: list)``
    """
    unknown = []
    contacts = []
    groups = []
    check_registered = []
    try:
        _, group_ids = get_groups(number=number)
    except Exception as exc:
        raise Exception(f"Unable to fetch groups for {number}") from exc
    for recipient in recipients:
        if version == 1:
            recipient = recipient.replace("_", "/")
        if j_search(f"[?id==`{recipient}`]", group_ids):
            groups.append(recipient)
            continue
        if re_search("[a-zA-Z/=]", recipient):
            unknown.append(recipient)
            continue
        check_registered.append(recipient)
    try:
        registered = is_registered(recipients=check_registered, number=number)
    except Exception as exc:
        raise Exception(
            "Unable to fetch network registration status for recipients"
        ) from exc
    for recipient in check_registered:
        if j_search(f"[?number==`{recipient}`]", registered):
            contacts.append(recipient)
            continue
        unknown.append(recipient)
    return unknown, contacts, groups


def is_registered(recipients: list, number: str):
    """
    Check for recipients Signal network registration status.

    Args:
        recipients (list)
        number (str)

    Returns:
        list: list of dictionaries ``{'number': '42', 'registered': True|False}``
    """
    recipients[:] = [re_sub("^([1-9])[0-9]+$", r"+\1", s) for s in recipients]
    res = jsonrpc(
        {
            "method": "getUserStatus",
            "params": {
                "account": number,
                "recipient": recipients,
            },
        }
    )
    return j_search(
        "[?isRegistered].{number: number, registered: isRegistered}", res.get("result")
    )


def get_group_response(group: dict):
    """
    create reponse for group details
    """
    return {
        "blocked": group.get("isBlocked"),
        "id": group.get("id"),
        "invite_link": group.get("groupInviteLink"),
        "members": list(map(lambda d: d["number"], group.get("members"))),
        "name": group.get("name"),
        "pending_invites": group.get("pendingMembers"),
        "pending_requests": group.get("requestingMembers"),
        "message_expiration_timer": group.get("messageExpirationTimer"),
        "admins": list(map(lambda d: d["number"], group.get("admins"))),
        "description": group.get("description"),
    }


def get_groups(number: str, groupid: str = ""):
    """
    get groups
    """
    if not number:
        return (False, "Missing number")
    try:
        groups = jsonrpc(
            {
                "method": "listGroups",
                "params": {
                    "account": number,
                },
            }
        ).get("result", [])
        if groupid:
            match = j_search(f"[?id==`{groupid}`]", groups)
            if match:
                return (True, get_group_response(match[0]))
        result = []
        for group in groups:
            result.append(get_group_response(group))
        return (True, result)
    # pylint: disable=broad-except
    except Exception as err:
        return (False, err)


def do_decode_attachments(attachments, uuid):
    """
    decode base64 attachments and dump the decoded
    content to disk for sending out later
    """
    decoded_attachments = []
    for index, attachment in enumerate(attachments):
        try:
            attachment_io_bytes = BytesIO()
            attachment_io_bytes.write(b64decode(attachment))
            extension = guess_extension(
                from_buffer(attachment_io_bytes.getvalue(), mime=True)
            )
            _, filename = mkstemp(prefix=f"{uuid}_{index}_", suffix=f".{extension}")
            with open(filename, "wb") as f_h:
                f_h.write(b64decode(attachment))
            decoded_attachments.append(filename)
        # pylint: disable=broad-except
        except Exception as err:
            logger.error("unable to decode attachment: %s", err)
    return decoded_attachments
