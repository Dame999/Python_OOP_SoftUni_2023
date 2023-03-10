from project.room import Room


class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number: int, people: int):
        try:
            room = [r for r in self.rooms if r.number == room_number][0]
        except IndexError:
            pass

        if room.capacity >= people + room.guests:
            room.take_room(people)
            self.guests += people

    def free_room(self, room_number):
        try:
            room = [r for r in self.rooms if r.number == room_number][0]
        except IndexError:
            pass
        self.guests -= room.guests
        room.free_room()

    def status(self):
        free_rooms = ', '.join(str(r.number) for r in self.rooms if not r.is_taken)
        taken_rooms = ', '.join(str(r.number) for r in self.rooms if r.is_taken)
        return f"Hotel {self.name} has {self.guests} total guests\n" \
               f"Free rooms: {free_rooms}\n" \
               f"Taken rooms: {taken_rooms}"
