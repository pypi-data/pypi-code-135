import json
from urllib.request import urlopen
import re


def fm_match_data(match_id: str) -> tuple:
    """Returns metadata and match data for a given match id

    Args:
        match_id (str): id of a match

    Returns:
        tuple: match data
            dict: metadata information
            list: events
            list: shots
            list: bench players
            list starters
            list: players not available
            list: shootout
    """

    assert isinstance(match_id, str), "match_id must be a string"

    url = f"https://www.fotmob.com/api/matchDetails?matchId={match_id}"

    response = urlopen(url)
    data = json.loads(response.read())

    general = data.get("general")
    header = data.get("header")
    content = data.get("content")
    matchFacts = content.get("matchFacts")
    matchStats = content.get("stats").get("stats")
    shotmap = content.get("shotmap").get("shots")
    lineup = content.get("lineup")

    metadata = {}
    metadata["id"] = general.get("matchId")
    metadata["date"] = header.get("status").get("startDateStr")
    metadata["time"] = matchFacts.get("infoBox").get("Match Date").get("timeFormatted")
    metadata["league_id"] = general.get("leagueId")
    metadata["league"] = general.get("leagueName")
    metadata["perent_league_id"] = general.get("parentLeagueId")
    metadata["parent_league"] = general.get("parentLeagueName")
    metadata["country"] = general.get("countryCode")
    metadata["season"] = general.get("parentLeagueSeason")
    metadata["matchweek"] = general.get("matchRound")
    metadata["team_x"] = general.get("homeTeam").get("name")
    metadata["team_y"] = general.get("awayTeam").get("name")
    metadata["id_x"] = general.get("homeTeam").get("id")
    metadata["id_y"] = general.get("awayTeam").get("id")
    metadata["color_x"] = general.get("teamColors").get("home")
    metadata["color_y"] = general.get("teamColors").get("away")
    metadata["score_x"] = header.get("teams")[0].get("score")
    metadata["score_y"] = header.get("teams")[1].get("score")
    metadata["reason"] = header.get("status").get("reason").get("long")
    try:
        metadata["highlights"] = matchFacts.get("highlights").get("url")
    except AttributeError:
        metadata["highlights"] = None
    stadium = matchFacts.get("infoBox").get("Stadium")
    metadata["venue"] = stadium.get("name")
    metadata["city"] = stadium.get("city")
    metadata["country"] = stadium.get("country")
    metadata["lat"] = stadium.get("lat")
    metadata["long"] = stadium.get("long")
    metadata["referee"] = matchFacts.get("infoBox").get("Referee").get("text")
    metadata["attendance"] = matchFacts.get("infoBox").get("Attendance")
    metadata["player_of_match"] = " ".join(
        matchFacts.get("playerOfTheMatch").get("name").values()
    )
    metadata["player_of_match_id"] = matchFacts.get("playerOfTheMatch").get("id")

    eventList = []
    events = matchFacts.get("events")["events"]
    score = "0:0"
    for e in events:
        mydict = {}
        mydict["minute"] = e.get("time")
        mydict["minute_stoppage"] = e.get("overloadTime")
        mydict["event"] = e.get("type")

        mydict["score_pre"] = score

        if mydict["event"] == "Goal":
            mydict["player1"] = e.get("player").get("name")
            mydict["player1_id"] = e.get("player").get("id")
            mydict["player1_url"] = e.get("player").get("profileUrl")
            mydict["player2"] = None

            try:
                mydict["player2_name"] = re.findall(
                    "(?<=assist by ).*$", e.get("assistStr")
                )[0]
            except TypeError:
                mydict["player2_name"] = None
            mydict["player2_id"] = e.get("assistPlayerId")
            mydict["player2_url"] = e.get("assistProfileUrl")
            newScore = e.get("newScore")
            mydict["score_post"] = str(newScore[0]) + ":" + str(newScore[1])
            score = mydict["score_post"]
            mydict["own_goal"] = False if e.get("ownGoal") is None else True
            mydict["is_penalty"] = (
                True if e.get("goalDescription") == "Penalty" else False
            )
            mydict["is_penalty_shootout"] = (
                False if e.get("isPenaltyShootoutEvent") is False else True
            )

        elif mydict["event"] == "Card":
            mydict["player1"] = e.get("player").get("name")
            mydict["player1_id"] = e.get("player").get("id")
            mydict["player1_url"] = e.get("player").get("profileUrl")
            mydict["card"] = e.get("card")

        elif mydict["event"] == "Substitution":
            swap = e.get("swap")
            mydict["player1"] = swap[0].get("name")
            mydict["player1_id"] = swap[0].get("id")
            mydict["player1_url"] = swap[0].get("profileUrl")
            mydict["player2"] = swap[1].get("name")
            mydict["player2_id"] = swap[1].get("id")
            mydict["player2_url"] = swap[1].get("profileUrl")
            mydict["score_post"] = score

        elif mydict["event"] == "AddedTime":
            mydict["minutes_added"] = e.get("minutesAddedStr").split()[1]

        elif mydict["event"] == "Half":
            continue

        eventList.append(mydict)

    try:
        shootoutList = []
        penalty_events = matchFacts.get("events")["penaltyShootoutEvents"]
        shootout_score = "0:0"
        for p in penalty_events:
            mydict = {}
            mydict["event"] = p.get("type")
            mydict["shooter"] = p.get("nameStr")
            mydict["shooter_id"] = p.get("player").get("id")
            mydict["shooter_url"] = p.get("profileUrl")
            mydict["score_pre"] = shootout_score
            try:
                newScore = p.get("penShootoutScore")
                mydict["score_post"] = str(newScore[0]) + ":" + str(newScore[1])
                shootout_score = mydict["score_post"]
            except TypeError:
                mydict["score_post"] = shootout_score

            shootoutList.append(mydict)
    except TypeError:
        shootoutList = None

    stats = {}
    for s in matchStats[1:]:
        for i in s.get("stats"):
            if i.get("stats") != [None, None]:

                if "xG" in i.get("title"):
                    val_x = float(i.get("stats")[0])
                    val_y = float(i.get("stats")[1])
                else:
                    val_x = i.get("stats")[0]
                    val_y = i.get("stats")[1]

                stats[i.get("title").replace(" ", "_").lower() + "_x"] = val_x
                stats[i.get("title").replace(" ", "_").lower() + "_y"] = val_y

    shotList = []
    for shot in shotmap:
        mydict = {}
        mydict["id"] = shot.get("id")
        mydict["minute"] = shot.get("min")
        mydict["minute_stoppage"] = shot.get("minAdded")
        mydict["period"] = shot.get("period")
        mydict["team_id"] = shot.get("teamId")
        mydict["player"] = shot.get("playerName")
        mydict["player_id"] = shot.get("playerId")
        mydict["situation"] = shot.get("situation")
        mydict["shot_type"] = shot.get("shotType")
        mydict["outcome"] = shot.get("eventType")
        mydict["x"] = shot.get("x")
        mydict["y"] = shot.get("y")
        mydict["is_blocked"] = shot.get("isBlocked")
        mydict["is_on_target"] = shot.get("isOnTarget")
        mydict["is_own_goal"] = shot.get("isOwnGoal")
        mydict["blocked_x"] = shot.get("blockedX")
        mydict["blocked_y"] = shot.get("blockedY")
        mydict["goal_crossed_y"] = shot.get("goalCrossedY")
        mydict["goal_crossed_z"] = shot.get("goalCrossedZ")
        mydict["xG"] = shot.get("expectedGoals")
        mydict["xGOT"] = shot.get("expectedGoalsOnTarget")
        on_goal = shot.get("onGoalShot")
        mydict["on_goal_x"] = on_goal.get("x")
        mydict["on_goal_y"] = on_goal.get("y")
        mydict["on_goal_zoom_ratio"] = on_goal.get("zoomRatio")

        shotList.append(mydict)

    benchPlayerList = []
    startPlayerList = []

    for i in lineup.get("lineup"):
        idx = lineup.get("lineup").index(i)
        team_id = i.get("teamId")
        for b in i.get("bench"):
            mydict = {}
            mydict["team_id"] = team_id
            mydict["opta_id"] = b.get("usingOptaId")
            mydict["player_id"] = b.get("id")
            mydict["player_name"] = " ".join(b.get("name").values())
            mydict["player_url"] = b.get("pageUrl")
            mydict["shirt_number"] = b.get("shirt")
            mydict["time_subbed_on"] = b.get("timeSubbedOn")
            mydict["time_subbed_off"] = b.get("timeSubbedOff")
            mydict["minutes_played"] = b.get("minutesPlayed")
            mydict["usual_position"] = b.get("usualPosition")
            mydict["role"] = b.get("role")
            mydict["is_captain"] = b.get("isCaptain")
            mydict["rating"] = b.get("rating").get("num")
            mydict["fantasy_points"] = b.get("fantasyScore").get("num")
            benchPlayerList.append(mydict)

        mgr = i.get("coach")[0]
        if idx == 0:
            metadata["manager_x"] = " ".join(mgr.get("name").values())
            metadata["manager_id_x"] = mgr.get("id")
            metadata["manager_url_x"] = mgr.get("pageUrl")
        else:
            metadata["manager_y"] = " ".join(mgr.get("name").values())
            metadata["manager_id_y"] = mgr.get("id")
            metadata["manager_url_y"] = mgr.get("pageUrl")

        for j in i.get("players"):
            for k in j:
                mydict = {}
                mydict["team_id"] = team_id
                mydict["opta_id"] = k.get("usingOptaId")
                mydict["player_id"] = k.get("id")
                mydict["player_name"] = " ".join(k.get("name").values())
                mydict["player_url"] = k.get("pageUrl")
                mydict["shirt_number"] = k.get("shirt")
                mydict["time_subbed_on"] = k.get("timeSubbedOn")
                mydict["time_subbed_off"] = k.get("timeSubbedOff")
                mydict["minutes_played"] = k.get("minutesPlayed")
                mydict["position"] = k.get("positionStringShort")
                mydict["usual_position"] = k.get("usualPosition")
                mydict["role"] = k.get("role")
                mydict["is_captain"] = k.get("isCaptain")
                mydict["fantasy_points"] = k.get("fantasyScore").get("num")
                mydict["minutes"] = k.get("minutesPlayed")

                playerStats = k.get("stats")[0].get("stats")
                mydict["rating"] = playerStats.get("FotMob rating")
                mydict["goals"] = playerStats.get("Goals")
                mydict["assists"] = playerStats.get("Assists")
                mydict["total_shots"] = playerStats.get("Total shots")
                mydict["accurate_passes"] = playerStats.get("Accurate passes")
                mydict["chances_created"] = playerStats.get("Chances created")
                mydict["conceded_penalty"] = playerStats.get("Conceded penalty")
                mydict["xA"] = playerStats.get("Expected assists (xA)")

                try:
                    playerStatsAttack = k.get("stats")[1].get("stats")
                    mydict["touches"] = playerStatsAttack.get("Touches")
                    mydict["successful_dribbles"] = playerStatsAttack.get(
                        "Successful dribbles"
                    )
                    mydict["accurate_crosses"] = playerStatsAttack.get(
                        "Accurate crosses"
                    )
                    mydict["accurate_long_balls"] = playerStatsAttack.get(
                        "Accurate long balls"
                    )
                    mydict["dispossessed"] = playerStatsAttack.get("Dispossessed")

                    playerStatsDefense = k.get("stats")[2].get("stats")
                    mydict["tackles_won"] = playerStatsDefense.get("Tackles won")
                    mydict["clearances"] = playerStatsDefense.get("Clearances")
                    mydict["interceptions"] = playerStatsDefense.get("Interceptions")
                    mydict["recoveries"] = playerStatsDefense.get("Recoveries")

                    playerStatsDuels = k.get("stats")[3].get("stats")
                    mydict["ground_duels_won"] = playerStatsDuels.get(
                        "Ground duels won"
                    )
                    mydict["aerial_duels_won"] = playerStatsDuels.get(
                        "Aerial duels won"
                    )
                    mydict["was_fouled"] = playerStatsDuels.get("Was fouled")
                    mydict["fouls_committed"] = playerStatsDuels.get("Fouls committed")
                except IndexError:
                    mydict["accurate_long_balls"] = playerStats.get(
                        "Accurate long balls"
                    )
                    mydict["touches"] = playerStats.get("Touches")

                mydict["saves"] = playerStats.get("Saves")
                mydict["goals_conceded"] = playerStats.get("Goals conceded")
                mydict["xGOT_faced"] = playerStats.get("xGOT faced")
                mydict["diving_save"] = playerStats.get("Diving save")
                mydict["saves_inside_box"] = playerStats.get("Saves inside box")
                mydict["acted_as_sweeper"] = playerStats.get("Acted as sweeper")
                mydict["punches"] = playerStats.get("Punches")
                mydict["throws"] = playerStats.get("Throws")
                mydict["high_claims"] = playerStats.get("High claim")
                mydict["recoveries"] = playerStats.get("Recoveries")

                startPlayerList.append(mydict)

    if lineup.get("usingOptaLineup"):
        metadata["lineup_source"] = "Opta"
    elif lineup.get("usingEnetpulseLineup"):
        metadata["lineup_source"] = "Enetpulse"
    else:
        metadata["lineup_source"] = "Other"

    metadata["formation_x"] = lineup.get("lineup")[0].get("lineup")
    metadata["formation_y"] = lineup.get("lineup")[1].get("lineup")
    metadata["team_x_rating"] = lineup.get("teamRatings").get("home").get("num")
    metadata["team_y_rating"] = lineup.get("teamRatings").get("away").get("num")

    try:
        matchNaPlayers = lineup.get("naPlayers").get("naPlayersArr")
        naPlayerList = []
        side = "team_x"
        for j in matchNaPlayers:
            for k in j:
                mydict = {}
                mydict["side"] = side
                mydict["player_id"] = k.get("id")
                mydict["player_name"] = k.get("naInfo").get("name")
                mydict["player_url"] = k.get("pageUrl")
                mydict["reason"] = k.get("naInfo").get("naReason")
                mydict["expected_return"] = k.get("naInfo").get("expectedReturn")
                naPlayerList.append(mydict)
            side = "team_y"
    except AttributeError:
        naPlayerList = None

    return (
        metadata,
        eventList,
        shotList,
        benchPlayerList,
        startPlayerList,
        naPlayerList,
        shootoutList,
    )
