import asyncio
import platform
import re
from csv import DictReader

import unidecode

from . import request

if platform.system() == "Windows":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


def get_runemetrics(players: list[str]):
    """
    Takes a list of players and accesses the runemetrics API endpoint.  The results are aggregated and return as json.
    :param players:
    :return:
    """
    urls = [
        f"https://apps.runescape.com/runemetrics/profile/profile?user={player}&activities=20"
        for player in players
    ]
    return asyncio.run(request.get(urls=urls, expected_response="json"))


def get_clan_data(clans: list[str]) -> str:
    urls = [
        f"https://services.runescape.com/m=clan-hiscores/members_lite.ws?clanName={clan}"
        for clan in clans
    ]
    return asyncio.run(request.get(urls=urls, expected_response="csv"))


def get_clan_members(clans: list[str]):
    clan_members = get_clan_data(clans=clans)

    list_of_members = []
    for clan in clan_members:
        d_r = DictReader(unidecode.unidecode(clan).splitlines())
        list_of_members.append([elem["Clanmate"] for elem in list(d_r)])

    return list_of_members


def get_player_uuid(player: str) -> str:
    urls = [f"https://secure.runescape.com/m=group_hiscores/v1/players?name={player}"]
    response = asyncio.run(request.get(urls=urls, expected_response="json"))

    members = {}
    j = 0
    for entry in response:
        if "message" not in entry:
            for i in range(len(entry[0]["members"])):
                if entry[0]["members"][i]["id"] not in members:
                    members.update({player: entry[0]["members"][i]["id"]})
        else:
            result = re.search(r"User\swith\sid:\s\b(\d*)\b", entry["message"])
            members.update({player: int(result.group(1))})
            j += 1

    return members[player]
