import pyterri.utils as utils

def getClans(limit: int = None):
    """
    Get clan data, up to limit if supplied
    """
    clans = utils.requestClanData()
    out = list()

    if limit == None:
        limit = len(clans)

    for clan_index in range(limit):
        clans[clan_index] = clans[clan_index].replace(" ", "")
        clan_data = clans[clan_index].split(",")

        try:
            clans[clan_index] = {
                "clan": clan_data[1],
                "rank": clan_data[0],
                "score": clan_data[2]
            }
        except IndexError:
            utils.addProblem(clan_data)

        out.append(clans[clan_index])

    return out