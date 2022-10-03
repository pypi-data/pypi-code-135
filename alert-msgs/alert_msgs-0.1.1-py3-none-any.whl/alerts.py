import argparse
from typing import Optional, Sequence, Union

from .components import MsgComp, Text
from .emails import send_email
from .settings import alert_settings
from .slack import send_slack_message


def send_alert(
    components: Sequence[MsgComp],
    methods: Optional[Union["email", "slack"]] = None,
    **kwargs,
) -> bool:
    """Send a message via Slack and/or Email.

    Args:
        components (Sequence[MsgComp]): The components to include in the message.
        methods (Optional[Union[&quot;email&quot;, &quot;slack&quot;]], optional): Where the message should be sent. Defaults to environmental variables.

    Returns:
        bool: Whether the message was sent successfully.
    """
    funcs = []
    if methods:
        if isinstance(methods, str):
            methods = [methods]
        if "email" in methods:
            funcs.append(send_email)
        if "slack" in methods:
            funcs.append(send_slack_message)
    else:
        if alert_settings.alert_slack:
            funcs.append(send_slack_message)
        if alert_settings.send_email:
            funcs.append(send_email)
    if not funcs:
        raise ValueError(f"Unknown method '{methods}'. Valid choices: slack, email.")
    return all(func(components=components, **kwargs) for func in funcs)



def text_alert_cmd() -> bool:
    parser = argparse.ArgumentParser()
    parser.add_argument('text')
    parser.add_argument('--slack', action='store_true')
    parser.add_argument('--email', action='store_true')
    args = parser.parse_args()
    methods = []
    if args.slack:
        methods.append('slack')
    if args.email:
        methods.append('email')
    return send_alert(components=[Text(args.text)], methods=methods or None)
