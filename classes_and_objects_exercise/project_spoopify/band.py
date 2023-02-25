from project_spoopify.album import Album, Song


class Band:
    def __init__(self, name: str):
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."

        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str):
        try:
            album_to_remove = [alb for alb in self.albums if alb.name == album_name][0]
            if album_to_remove.published:
                return f"Album has been published. It cannot be removed."
        except IndexError:
            return f"Album {album_name} is not found."

        self.albums.remove(album_to_remove)
        return f"Album {album_name} has been removed."

    def details(self):
        album_details = '\n'.join(alb.details() for alb in self.albums)
        return f"Band {self.name}" + "\n" + album_details + "\n"


song = Song("Running in the 90s", 3.45, False)
print(song.get_info())
album = Album("Initial D", song)
second_song = Song("Around the World", 2.34, False)
print(album.add_song(second_song))
print(album.details())
print(album.publish())
band = Band("Manuel")
print(band.add_album(album))
print(band.remove_album("Initial D"))
print(band.details())
