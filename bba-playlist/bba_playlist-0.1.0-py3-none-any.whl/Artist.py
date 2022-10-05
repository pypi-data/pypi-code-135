import json

class Artist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def get_songs(self):
        return self.songs

    def get_name(self) -> str:
        return self.name

    def copy_songs(self, artist):
        for song in artist.get_songs():
            self.add_song(song)

    def add_song(self, song_name):
        if song_name not in self.songs:
            self.songs.append(song_name)

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)