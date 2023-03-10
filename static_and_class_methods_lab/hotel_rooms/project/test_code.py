from project.hotel import Hotel
from project.room import Room

room = Room(1, 3)
hotel = Hotel("Some Hotel")
print(room.is_taken)
room.take_room(4)
print(room.is_taken)