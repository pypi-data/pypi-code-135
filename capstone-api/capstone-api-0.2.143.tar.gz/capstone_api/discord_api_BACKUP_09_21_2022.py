# coding: utf-8
from .utils.requests_api import RequestsAPI
from .utils.tools import filterObjects
from configparser import ConfigParser
from collections import Counter
from pathlib import Path
import requests
import time
import re

class DiscordAPI(RequestsAPI):
    """Discord web api connector"""

    def __init__(self, config_path=str(Path(Path.home(), '.config', 'capstone_api')), config_file='capstone_api.ini', config_key="discord"):
        """Configs"""
        capstone_api_ini = Path(config_path, config_file)
        if capstone_api_ini.exists():
            config = ConfigParser()
            config.read(capstone_api_ini)
            conf = dict(config[config_key].items())
            self.API_URL = conf["api_url"]
            self.API_KEY = conf["api_key"]
            self.GUILD_ID = conf["guild_id"]
            self.BOT_ID = conf["bot_id"]
            self.INSTRUCTOR_ID = conf["instructor_id"]
            self.TA_ID = conf.get("ta_id")
            self.STUDENT_ID = conf.get("student_id")

            self.users = {}
            self.members = {}
            self.data = []
            self.categories = []
            self.channels = []
            self.team_categories = []
            super().__init__(self.API_URL, self.API_KEY)

    def setMembers(self, delay=0):
        """Store Guild Members"""
        if not self.members:
            path = f'/guilds/{self.GUILD_ID}/members'
            members = self.get(path, params={"limit": 200})
            self.members = members

    def getMembers(self, delay=0):
        """Get Guild Members"""
        if not self.members:
            self.setMembers(delay=delay)
        return self.members

    def getMember(self, username=''):
        """Get Member by UserName"""
        # -- username = "enormouspoon"
        if not self.members:
            self.getMembers(delay=0)
        return next(filter(lambda v: v["user"]["username"] == username, self.members))

    def getTeachers(self, delay=0):
        """Get Teachers (members with role=instructors)"""
        if not self.members:
            self.setMembers(delay=delay)
        return list(filter(lambda x: self.INSTRUCTOR_ID in x["roles"], self.members))

    def getTAs(self, delay=0):
        """Get Students (members with role=tas)"""
        if not self.members:
            self.setMembers(delay=delay)
        return list(filter(lambda x: self.TA_ID in x["roles"], self.members))

    def getStudents(self, delay=0):
        """Get Students (members with role=students)"""
        if not self.members:
            self.setMembers(delay=delay)
        return list(filter(lambda x: self.STUDENT_ID in x["roles"], self.members))

    def setUsers(self, delay=0):
        """Get a List of Users (members) in Guild"""
        if not self.users:
            path = f'/guilds/{self.GUILD_ID}/members'
            members = self.get(path, params={"limit": 200})
            instructors = ["そこたろ", "Rick Martin", "Chase Cotton"]
            teachers = filterObjects(members, keys=["username"], accepts=instructors)
            self.members = members
            self.users = {}

            for t in teachers:
                name = t["user"]["username"].replace("そこたろ", "Teddy Katayama")
                name = "-".join(n.lower() for n in name.split())
                self.users[t["user"]["id"]] = {"name": name, "messages": []}
            print(self.users)

            for team_category in self.getTeamCategories():
                for team_channel in self.getTeamChannels(team_category["id"], students_only=True):
                    name = team_channel["name"]
                    messages = self.getMessages(team_channel["id"])
                    if messages:
                        s_id = Counter([m["author"]["id"] for m in messages]).most_common()[0][0]
                    else:
                        n = name.split('-')
                        n = [" ".join([nn.capitalize() for nn in n])] + list(map(str.capitalize, n)) + n
                        tmp = filterObjects(members, keys=["nick", "username"], accepts=n)[0]
                        s_id = tmp["user"]["id"]
                    self.users[s_id] = {"name": name, "messages": messages}
                    print(f'{s_id}: "{name}", "num_messages": {len(messages)}')
                time.sleep(delay)
            self.users['570065962129424388'] = {"name": self.users['752573259135975485']['name'], "messages": []}
            self.users['710728926141481000'] = {"name": self.users['129996057827344384']["name"], "messages": []}

    def getUsers(self, delay=0):
        """Get a LIst of Users (members) in Guild"""
        if not self.users:
            self.setUsers(delay=delay)
        return self.users

    def getUser(self, channel_name=''):
        """Get User by Channel Name Reference"""
        if not self.users:
            self.getUsers(delay=0)
        return next(filter(lambda v: v["name"] == channel_name, self.users.values()))

    def setCategories(self, *args, **kwargs):
        """Store all Categories (type == 4)"""
        if not self.data:
            path = f'/guilds/{self.GUILD_ID}/channels'
            self.data = self.get(path)
        categories = list(filter(lambda c: c["type"] == 4, self.data))
        self.categories = sorted(categories, key=lambda x: x['name'].lower())

    def getCategories(self, *args, **kwargs):
        """Get all categories (TYPE = 4)"""
        if not self.categories:
            self.setCategories()
        return self.categories

    def getTeamCategories(self, *args, **kwargs):
        """Get Student Team Category Channels"""
        if not self.categories:
            self.setCategories()
        if not self.team_categories:
            self.team_categories = list(filter(lambda c: not c["name"].startswith("---"), self.categories))
        return self.team_categories

    def findCategory(self, name=''):
        """Find Category by name (TYPE = 4)"""
        if not self.categories:
            self.setCategories()

        categories = list(filter(lambda c: c["name"].lower() == name.lower(), self.categories))
        if len(categories) == 1:
            return categories[0]
        return sorted(categories, key=lambda x: x['name'].lower())

    def createCategory(self, name='', allow='1024', deny='0'):
        """Create Category
        Category is TYPE = 4
        Students can view but nothing else
        """
        path = f'/guilds/{self.GUILD_ID}/channels'
        payload = {
            'type': 4,
            'name': name,
            'permission_overwrites': [
                # '139586817088' or '1024',
                {'id': self.STUDENT_ID, 'type': 0, 'allow': allow, 'deny': deny},
                {'id': self.INSTRUCTOR_ID, 'type': 0, 'allow': '536804850935', 'deny': '0'},
                {'id': self.BOT_ID, 'type': 0, 'allow': '536804850935', 'deny': '0'}
            ]
        }
        data = self.post(path, json=payload)
        return data

    def deleteCategory(self, category_id=0):
        """Delete channel"""
        path = f'/channels/{category_id}'
        return self.delete(path)

    def setChannels(self, *args, **kwargs):
        """Store all Channels (type == 0)"""
        if not self.data:
            path = f'/guilds/{self.GUILD_ID}/channels'
            self.data = self.get(path)
        channels = list(filter(lambda c: c["type"] == 0, self.data))
        self.channels = sorted(channels, key=lambda x: x['name'].lower())

    def getChannels(self, *args, **kwargs):
        """Get all channels"""
        if not self.channels:
            self.setChannels()
        return self.channels

    def getTeamChannels(self, category_id: int, students_only=False, info_only=False):
        """Get all Channels in a Team Category"""
        if not self.channels:
            self.setChannels()

        team_channels = list(filter(lambda c: c["parent_id"] == category_id, self.channels))
        if not students_only and not info_only:
            return team_channels
        if info_only:
            student_channels = filterObjects(team_channels, keys=["name"], accepts=["info"])
        if students_only:
            student_channels = filterObjects(team_channels, keys=["name"], rejects=["instructor-notes", "info"])
        return sorted(student_channels, key=lambda x: x['position'])

    def findChannel(self, name='', category_id=0):
        """Search for a channel"""
        if not self.channels:
            self.setChannels()
        if category_id:
            channels = list(filter(lambda c: c["parent_id"] == category_id and c["name"] == name.lower(), self.channels))
        else:
            channels = list(filter(lambda c: c["name"] == name.lower(), self.channels))
        if len(channels) == 1:
            return channels[0]
        return sorted(channels, key=lambda x: x['name'].lower())

    def createChannel(self, name='', category_id=0, allow='1024', deny='0'):
        """
        Create Channel
        Be sure to check the allow permissions...

        1024 == "View Channels"
        """
        path = f'/guilds/{self.GUILD_ID}/channels'
        payload = {
            'type': 0,
            'name': name,
            'parent_id': category_id,
            'permission_overwrites': [
                # '139586817088' or '1024',
                {'id': self.STUDENT_ID, 'type': 0, 'allow': allow, 'deny': deny},
                {'id': self.INSTRUCTOR_ID, 'type': 0, 'allow': '536804850935', 'deny': '0'},
                {'id': self.BOT_ID, 'type': 0, 'allow': '536804850935', 'deny': '0'},
                {'id': self.TA_ID, 'type': 0, 'allow': '536804850935', 'deny': '0'},
            ]
        }
        return self.post(path, json=payload)

    def getChannel(self, name='', category_id=0):
        channels = self.findChannel(name=name, category_id=category_id)
        if isinstance(channels, dict):
            channels.update({'messages': self.getMessages(channel_id=channels["id"])})
        if isinstance(channels, list):
            for channel in channels:
                channel.update({'messages': self.getMessages(channel_id=channel["id"])})
        return channels

    def deleteChannel(self, channel_id=0):
        """Delete channel"""
        path = f'/channels/{channel_id}'
        return self.delete(path)

    def editChannelPermissions(self, channel_id=0, allow="0", deny="1024"):
        """Edit Channel Permissions"""
        path = f'/channels/{channel_id}/permissions/{self.GUILD_ID}'
        payload = {"id": channel_id, "allow": allow, "deny": deny, "type": 0}
        return self.put(path, json=payload)

    def createMessage(self, title='', message='', content='', embed=False, channel_id=0):
        """Create Message"""
        path = f'/channels/{channel_id}/messages'
        payload = {'tts': False}
        if embed:
            payload["embeds"] = [{'title': title, 'description': message}]
        else:
            if content:
                payload["content"] = content
            else:
                payload["content"] = f'...\n**{title}**\n\n{message}'

        return self.post(path, json=payload)

    def createImgMessage(self, img='', description='', channel_id=0):
        """Create Image Message"""
        path = f'/channels/{channel_id}/messages'
        payload = {
            'tts': False,
            'embeds': [{
                'image': {'url': img},
                'description': description,
            }]
        }
        return self.post(path, json=payload)

    def getMessages(self, channel_id=0, name=''):
        """Get all Messages in a Channel"""
        if channel_id:
            path = f'/channels/{channel_id}/messages'
            payload = {'limit': '100'}
            # return self.get(path, params=payload)
            data = self.get(path, params=payload)
            return sorted(data, key=lambda x: x['id'])
        return self.getUser(name)["messages"]
    # def sendCommand(self, application_id):

    def cloneMessage(self, msg={}, channel_id=0):
        """Attempt to clone a message from server to server"""
        path = f'/channels/{channel_id}/messages'
        # 'author': msg.get('author'),
        payload = {
            'tts': msg.get('tts'),
            'type': msg.get('type'),
            'flags': msg.get('flags'),
            'embeds': msg.get('embeds'),
            'content': msg.get('content'),
            'components': msg.get('components'),
            'attachments': msg.get('attachments'),
        }

        # -- change to file upload request
        if msg.get('attachments'):
            responses = []
            for a in payload.pop("attachments"):
                files = { "file": (a["filename"], requests.get(a["url"]).content) }
                responses.append(self.post(path, data=payload, files=files))
                time.sleep(1)
            return responses

        if msg.get('embeds'):
            if msg["embeds"][0].get('description'):
                desc = msg["embeds"][0]['description']
                if ((desc.count('\n') > 10) and not (re.search(r'(\([1-9]{1}\)|specifically|UART)', desc))):
                    title = ''
                    stuff = ''
                    if msg["embeds"][0].get("title"):
                        temp = msg["embeds"][0].get("title").replace('**', '').strip() + '\n'
                        title = '** **\n```yaml\n' + temp + '```\n'
                    if msg.get('content'):
                        stuff = msg.get('content').strip() + '\n'
                    content = f'{title.strip()}{stuff}{msg["embeds"][0]["description"].strip()}'
                    payload.update({"content": content, "embeds": []})

        return self.post(path, json=payload)


    def deleteMessage(self, channel_id=0, message_id=0):
        """Delete a message in a channel"""
        path = f'/channels/{channel_id}/messages/{message_id}'
        return self.delete(path)


'''
d = DISCORD_API()
category = d.createCategory(name="TEST")
channel = d.createChannel(name="test", category_id=category["id"])
message = d.createMessage(title='title', message='message', channel_id=channel["id"])
'''
