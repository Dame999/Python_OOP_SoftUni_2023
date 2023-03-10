from math import ceil


class PhotoAlbum:
    PAGES = 4

    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(ceil(photos_count / cls.PAGES))

    def add_photo(self, label: str):
        for r in range(self.pages):
            if len(self.photos[r]) < PhotoAlbum.PAGES:
                self.photos[r].append(label)
                return f"{label} photo added successfully on page {r + 1} slot {len(self.photos[r])}"
        return "No more free slots"

    def display(self):
        result = ["-" * 11]
        for r in self.photos:
            result.append(("[] " * len(r)).strip())
            result.append("-" * 11)

        return '\n'.join(result)


album = PhotoAlbum(3)
for _ in range(8):
    album.add_photo("asdf")
print(album.display())