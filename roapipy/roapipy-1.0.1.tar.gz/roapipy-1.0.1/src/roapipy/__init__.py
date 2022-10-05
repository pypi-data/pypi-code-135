import requests, json

def checkrs(rs):
    el = requests.get("https://users.roblox.com/v1/users/authenticated", cookies={".ROBLOSECURITY": rs})
    el = json.loads(el.text)
    if "errors" in el:
        return None
    else:
        return True

class Client():
    def __init__(self, rosec=None):
        self.User = _User(rosec)
        self.Group = _Group(rosec)

class _User():
    def __init__(self, rosec):
        self._rosec = rosec
    
    def Info(self, id):
        el = requests.get(f"https://users.roblox.com/v1/users/{id}")
        el = json.loads(el.text)
        if "data" not in el:
            foo = requests.get("https://thumbnails.roblox.com/v1/users/avatar", params={"userIds": id, "size": "720x720", "format": "png"})
            foo = json.loads(foo.text)
            info = {
                "name": el["name"],
                "nick": el["displayName"],
                "id": el["id"],
                "creation": el["created"],
                "avatar": foo["data"][0]["imageUrl"]
            }
            return info
        else:
            return "That user doesn't exist"
    
    def Activity(self, id):
        params = {
            "userIds": [
                id
            ]
        }
        el = requests.post("https://presence.roblox.com/v1/presence/users", json=params)
        el = json.loads(el.text)
        if "errors" not in el:
            el = el["userPresences"][0]
            if el["userPresenceType"] == 0:
                type = "Offline"
            elif el["userPresenceType"] == 1:
                type = "Online"
            elif el["userPresenceType"] == 2:
                type = "In-Game"
            else:
                type = "Creating"
            info = {
                "type": type
            }
            return info
        else:
            return el["errors"][0]["message"]

    def Groups(self, id):
        el = requests.get(f"https://groups.roblox.com/v1/users/{id}/groups/roles")
        el = json.loads(el.text)
        if "errors" not in el:
            info = {}
            for foo in el["data"]:
                info[foo["group"]["name"]] = {
                    "Id": foo["group"]["id"],
                    "Role": {
                        "Name": foo["role"]["name"],
                        "Id": foo["role"]["id"]
                    }
                }
            return info
        else:
            return el["errors"][0]["message"]

class _Group():
    def __init__(self, rosec):
        self._rosec = rosec
    
    def Info(self, groupid):
        el = requests.get(f"https://groups.roblox.com/v1/groups/{groupid}")
        el = json.loads(el.text)
        foo = requests.get(f"https://thumbnails.roblox.com/v1/groups/icons", params={"groupIds": groupid, "size": "420x420", "format": "png"})
        foo = json.loads(foo.text)
        if "errors" not in el:
            info = {
                "name": el["name"],
                "id": el["id"],
                "description": el["description"],
                "members": el["memberCount"],
                "private": el["publicEntryAllowed"],
                "owner": {
                    "name": el["owner"]["username"],
                    "id": el["owner"]["userId"]
                },
                "avatar": foo["data"][0]["imageUrl"]
            }
            return info
        else:
            return el["errors"][0]["message"]
    
    def Roles(self, groupid):
        el = requests.get(f"https://groups.roblox.com/v1/groups/{groupid}/roles")
        el = json.loads(el.text)
        if "errors" not in el:
            all = {}
            for foo in el["roles"]:
                all[foo["name"]] = {
                    "id": foo["id"],
                    "rank": foo["rank"],
                    "holders": foo["memberCount"]
                }
            return all
        else:
            return el["errors"][0]["message"]
    
    def Shout(self, groupid, shout):
        rosec = self._rosec
        if rosec:
            rscheck = checkrs(rosec)
            if rscheck:
                el = requests.patch(f"https://groups.roblox.com/v1/groups/{groupid}/status", cookies={".ROBLOSECURITY": rosec}, json={"message": shout})
                el = requests.patch(f"https://groups.roblox.com/v1/groups/{groupid}/status", cookies={".ROBLOSECURITY": rosec}, json={"message": shout}, headers={"x-csrf-token": el.headers["x-csrf-token"]})
                el = json.loads(el.text)
                if "errors" in el:
                    return el["errors"][0]["message"]
                else:
                    return "Shouted"
            else:
                return "Your roblosecurity is invalid"
        else:
            return "You don't have a connected roblosecurity"
    
    def Accept(self, groupid, userid):
        rosec = self._rosec
        if rosec:
            rscheck = checkrs(rosec)
            if rscheck:
                el = requests.post(f"https://groups.roblox.com/v1/groups{groupid}/join-requests/users/{userid}", cookies={".ROBLOSECURITY": rosec})
                el = requests.post(f"https://groups.roblox.com/v1/groups{groupid}/join-requests/users/{userid}", cookies={".ROBLOSECURITY": rosec}, headers={"x-csrf-token": el.headers["x-csrf-token"]})
                el = json.loads(el.text)
                if "errors" in el:
                    return el["errors"][0]["message"]
                else:
                    return "Accepted"
            else:
                return "Your roblosecurity is invalid"
        else:
            return "You don't have a connected roblosecurity"
    
    def Rank(self, groupid, userid, rank):
        rosec = self._rosec
        if rosec:
            rscheck = checkrs(rosec)
            if rscheck:
                el = requests.get(f"https://users.roblox.com/v1/users/{userid}")
                el = json.loads(el.text)
                if "errors" not in el:
                    try:
                        rank = int(rank)
                        isint = True
                    except:
                        isint = None
                    if isint:
                        if rank <= 255:
                            el = requests.get(f"https://groups.roblox.com/v1/groups/{groupid}/roles")
                            el = json.loads(el.text)
                            if rank in [foo["rank"] for foo in el["roles"]]:
                                for bar in el["roles"]:
                                    if bar["rank"] == rank:
                                        rank = bar["id"]
                                el = requests.patch(f"https://groups.roblox.com/v1/groups/{groupid}/users/{userid}", data={"roleId": rank}, cookies={".ROBLOSECURITY": rosec})
                                el = requests.patch(f"https://groups.roblox.com/v1/groups/{groupid}/users/{userid}", data={"roleId": rank}, cookies={".ROBLOSECURITY": rosec}, headers={"x-csrf-token": el.headers["x-csrf-token"]})
                                el = json.loads(el.text)
                                if "errors" in el:
                                    return el["errors"][0]["message"]
                                else:
                                    return "Ranked"
                            else:
                                return "A rank with that id doesn't exist in that group"
                        else:
                            el = requests.get(f"https://groups.roblox.com/v1/roles", params={"ids": rank})
                            el = json.loads(el.text)
                            if "errors" in el:
                                return el["errors"][0]["message"]
                            else:
                                if el["data"][0]["groupId"] == groupid:
                                    el = requests.patch(f"https://groups.roblox.com/v1/groups/{groupid}/users/{userid}", data={"roleId": rank}, cookies={".ROBLOSECURITY": rosec})
                                    el = requests.patch(f"https://groups.roblox.com/v1/groups/{groupid}/users/{userid}", data={"roleId": rank}, cookies={".ROBLOSECURITY": rosec}, headers={"x-csrf-token": el.headers["x-csrf-token"]})
                                    el = json.loads(el.text)
                                    if "errors" in el:
                                        return el["errors"][0]["message"]
                                    else:
                                        return "Ranked"
                                else:
                                    return "That rank id doesn't belong to the group id sent"
                    else:
                        el = requests.get(f"https://groups.roblox.com/v1/groups/{groupid}/roles")
                        el = json.loads(el.text)
                        if rank.lower() in [foo["name"].lower() for foo in el["roles"]]:
                            for foo in el["roles"]:
                                if foo["name"] == rank:
                                    rank = foo["id"]
                            el = requests.patch(f"https://groups.roblox.com/v1/groups/{groupid}/users/{userid}", data={"roleId": rank}, cookies={".ROBLOSECURITY": rosec})
                            el = requests.patch(f"https://groups.roblox.com/v1/groups/{groupid}/users/{userid}", data={"roleId": rank}, cookies={".ROBLOSECURITY": rosec}, headers={"x-csrf-token": el.headers["x-csrf-token"]})
                            el = json.loads(el.text)
                            if "errors" in el:
                                return el["errors"][0]["message"]
                            else:
                                return "Ranked"
                        else:
                            return "That rank doesn't exist in that group"
                else:
                    return "An account with that id doesn't exist"
            else:
                return "Your roblosecurity is invalid"
        else:
            return "You don't have a connected roblosecurity"
    
    def Exile(self, groupid, userid):
        rosec = self._rosec
        if rosec:
            rscheck = checkrs(rosec)
            if rscheck:
                el = requests.delete(f"https://groups.roblox.com/v1/groups/{groupid}/users/{userid}", cookies={".ROBLOSECURITY": rosec})
                el = requests.delete(f"https://groups.roblox.com/v1/groups/{groupid}/users/{userid}", cookies={".ROBLOSECURITY": rosec}, headers={"x-csrf-token": el.headers["x-csrf-token"]})
                el = json.loads(el.text)
                if "errors" in el:
                    return el["errors"][0]["message"]
                else:
                    return "Exiled"
            else:
                return "Your roblosecurity is invalid"
        else:
            return "You don't have a connected roblosecurity"