# from project.song import Song
# 
# class Album:
# 
#     def __init__(self, name:str, *songs: Song):
#         self.name = name
#         self.published = False
#         self.songs = [*songs]
# 
#     def add_song(self, song: Song):
#         if self.published:
#             return "Cannot add songs. Album is published."
#         elif song in self.songs:
#             return "Song is already in the album."
#         elif song.single:
#             return f"Cannot add {song.name}. It's a single"
#         self.songs.append(song)
#         return f"Song {song.name} has been added to the album {self.name}."
# 
#     def remove_song(self, song_name: str):
#         if self.published:
#             return "Cannot remove songs. Album is published."
#         elif song_name not in self.songs:
#             return "Song is not in the album."
# 
#         self.songs.remove(song_name)
#         return f"Removed song {song_name} from album {self.name}."
# 
#     def publish(self):
#         if self.published:
#             return f"Album {self.name} is already published."
#         self.published = True
#         return f"Album {self.name} has been published."
# 
#     def details(self):
#         songs_details = "\n".join(f"== {s.get_info()}" for s in self.songs)
#         return f"Album {self.name}\n" \
#                f"{songs_details}"
from project.song import Song

class Album:
    def __init__(self, name: str, *songs: Song):
        self.name = name
        self.published = False
        self.songs = list(songs)

    def add_song(self, song: Song):
        if self.published:
            return "Cannot add songs. Album is published."
        elif song in self.songs:
            return "Song is already in the album."
        elif song.single:
            return f"Cannot add {song.name}. It's a single"
        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        if self.published:
            return "Cannot remove songs. Album is published."
        elif song_name not in [s.name for s in self.songs]:
            return "Song is not in the album."

        self.songs = [song for song in self.songs if song.name != song_name]
        return f"Removed song {song_name} from album {self.name}."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."
        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        songs_details = "\n".join(f"== {s.get_info()}" for s in self.songs)
        return f"Album {self.name}\n{songs_details}"