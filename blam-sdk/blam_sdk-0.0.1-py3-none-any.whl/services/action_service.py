import socket
from blam_sdk.services.base_service import BlamBaseService


class ActionService(BlamBaseService):
    def __init__(self, user=None, password=None):
        super().__init__("action", user, password)

    def get_actions(self):
        return self._get()

    def get_executions(self):
        return self._get("executions")

    def create_execution(self, action_id, asset_id="", parameters={}):
        return self._post(
            f"execute/{action_id}",
            {"asset_id": asset_id, "parameters": parameters},
        )

    def register_agent(
        self, name=socket.gethostname(), commands=[], action_ids=[]
    ):
        return self._post(
            "agents",
            {
                "name": name,
                "commands": commands,
                "action_ids": action_ids,
            },
        )

    def update_agent_capabilities(self, agent_id, commands=[], action_ids=[]):
        return self._put(
            f"agents/{agent_id}",
            {
                "commands": commands,
                "action_ids": action_ids,
            },
        )
