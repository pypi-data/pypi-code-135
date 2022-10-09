# from json import load
# from structures import *

# def load_json(game,filename):
#     json = load(open(filename))
#     for char_name,char_info in json["characters"].items():
#         game.add_char(Character(char_info["hp"],char_info["regen"],char_info["strength"]))
#     return json["player"]

# if __name__ == "__main__":
#     import pickle
#     pickle.dump(load_json("/Users/toby/Code/text-adventures-python/json-structured-adventures/maenoyd.json"),open("maenoyd.pickle","wb"))