import json

class Soundtrack:
    def __init__(self) -> None:
        self.artists = []

    def artist_exists(self, artist):
        for art in self.artists:
            if (artist.get_name() == art.get_name()):
                return art

        return None

    def add_artist(self, artist) -> None:
        art = self.artist_exists(artist)
        if (art is not None):
            art.copy_songs(artist)
            return

        self.artists.append(artist)    
    
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)