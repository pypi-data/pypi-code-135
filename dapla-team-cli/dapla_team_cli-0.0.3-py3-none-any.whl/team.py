"""Common models and functionality related to Dapla teams."""
from pydantic import BaseModel


class TeamInfo(BaseModel):
    """Information about a Dapla team.

    Attributes:
        name: Dapla team name, such as `demo-enhjoern-a`
        org_nr: The SSB organization number in Google Cloud
    """

    name: str
    org_nr: str
