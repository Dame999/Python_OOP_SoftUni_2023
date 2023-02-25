class Music:
    def __init__(self, title, artist, lyrics):
        self.title = title
        self.artist = artist
        self.lyrics = lyrics

    def print_info(self):
        return f'This is "{self.title}" from "{self.artist}"'

    def play(self):
        return f"{self.lyrics}"


music = Music("Whiplash", "Metallica", "Late at night, all systems go")
print(music.print_info())
print(music.play())
