import requests
from blam_sdk.agent_core import AgentConf
from blam_sdk.services import AssetService


class BaseActionHandler:
    def __init__(self, agent_conf: AgentConf):
        self.agent_conf = agent_conf
        self.asset_service = AssetService()

    def perform_action(self, message_body={}):
        raise NotImplementedError()

    def download_action_asset(self, message_body):
        download_url = self.asset_service.get_download_url(
            message_body["asset_id"]
        )
        file_ext = download_url.split("?")[0].split(".")[-1]
        req = requests.get(download_url, stream=True)
        with open(
            f"{self.agent_conf.working_dir}/{message_body['asset_id']}.{file_ext}",
            "wb",
        ) as f:
            for chunk in req.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)

    @staticmethod
    def get_action_config():
        raise NotImplementedError()
