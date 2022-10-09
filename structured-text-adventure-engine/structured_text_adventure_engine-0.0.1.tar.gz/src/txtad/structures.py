import copy

# import load_json


class GameEngineError(Exception):
    """ The error raised when information about the world is not sufficient or correct. """

class Game:
    def __init__(self,intro=None):
        self.end = False
        self.chars = []
        # {name:Location(hgekruthuerhgb)}
        self.locations = {}
        self.intro = intro
    
    def add_start_location(self,name,location):
        self.start_location = location
        self.locations[name] = location
    
    def add_locations(self,locations: dict):
        self.locations.update(locations)
    
    def set_player(self,player_char):
        self.player = player_char
        self.add_char(self.player)
    
    def add_char(self,char):
        self.chars.append(char)
    
    def add_chars(self,chars):
        self.chars += chars
    
    def regen_chars(self,times=1):
        for char in self.chars:
            char.regen(times)
    
    # def play(self):
    #     # check that the object contains all necerssery information
    #     necerssery_attributes = {
    #         "start_location": "The starting location is not provided.",
    #         "player": "The player character is not defined"
    #     }
    #     for attr in necerssery_attributes:
    #         if not hasattr(self,attr):
    #             raise GameEngineError(necerssery_attributes[attr])
        
    #     run.play(self)
    
    # def load_from_json(self,filename):
    #     self = load_json.load_json(self,filename)
    

class Weapon:
    def __init__(self,damage):
        self.damage = damage

class Character:
    def __init__(self,is_evil,hp,regen_rate,strength,weapons=[Weapon(10)]):
        self.total_hp = hp
        self.hp = copy.copy(hp)
        self.regen_rate = regen_rate
        self.strength = strength
        self.weapons = weapons
        self.is_evil = is_evil
    
    def regen(self,times=1):
        self.hp += self.regen_rate*times

class Location:
    def __init__(self,links,contents):
        self.links = links
        self.contents = contents
