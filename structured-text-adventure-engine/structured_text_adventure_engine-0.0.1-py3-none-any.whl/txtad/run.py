import copy

def ask_where_to_go(game,location):
    next_locations = ", ".join(location.links)
    next_location_name = input(f">>> You may go to {next_locations}. Where do you want to go?\n")
    if next_location_name in location.links:
        return game.locations[next_location_name]
    else:
        print(">>> That is not a valid location you can go to.")
        return ask_where_to_go(game,location)

def describe_location(game,location):
    print("You see {', '.join(location.contents)}.")

def play(game):
    def play(self):
        # check that the object contains all necerssery information
        necerssery_attributes = {
            "start_location": "The starting location is not provided.",
            "player": "The player character is not defined"
        }
        for attr in necerssery_attributes:
            if not hasattr(self,attr):
                # raise GameEngineError(necerssery_attributes[attr])
                pass
    game.current_location = copy.copy(game.start_location)
    if game.intro != None:
       print(game.intro)
    print()
    while True:
        describe_location(game,game.current_location)
        game.current_location = ask_where_to_go(game,game.current_location)
    