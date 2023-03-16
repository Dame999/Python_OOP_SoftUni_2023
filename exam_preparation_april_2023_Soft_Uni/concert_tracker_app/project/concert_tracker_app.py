from typing import List

from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.musician import Musician
from project.band_members.singer import Singer
from project.concert import Concert


class ConcertTrackerApp:
    def __init__(self):
        self.bands: List[Band] = []
        self.musicians: List[Musician] = []
        self.concerts: List[Concert] = []

    def create_musician(self, musician_type: str, name: str, age: int):
        valid_musician_types = ["Guitarist", "Drummer", "Singer"]
        if musician_type not in valid_musician_types:
            raise ValueError("Invalid musician type!")

        try:
            musician = [m for m in self.musicians if m.name == name][0]
            raise Exception(f"{name} is already a musician!")
        except IndexError:
            if musician_type == "Drummer":
                self.musicians.append(Drummer(name, age))
            elif musician_type == "Singer":
                self.musicians.append(Singer(name, age))
            elif musician_type == "Guitarist":
                self.musicians.append(Guitarist(name, age))

            return f"{name} is now a {musician_type}."

    def create_band(self, name: str):
        try:
            band = [b for b in self.bands if b.name == name][0]
            raise Exception(f"{name} band is already created!")
        except IndexError:
            self.bands.append(Band(name))
            return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        try:
            concert = [c for c in self.concerts if c.place == place][0]
            raise Exception(f"{place} is already registered for {concert.genre} concert!")
        except IndexError:
            self.concerts.append(Concert(genre, audience, ticket_price, expenses, place))
            return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        try:
            musician = [m for m in self.musicians if m.name == musician_name][0]
        except IndexError:
            raise Exception(f"{musician_name} isn't a musician!")

        try:
            band = [b for b in self.bands if b.name == band_name][0]
        except IndexError:
            raise Exception(f"{band_name} isn't a band!")

        band.members.append(musician)
        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        try:
            band = [b for b in self.bands if b.name == band_name][0]
        except IndexError:
            raise Exception(f"{band_name} isn't a band!")

        try:
            musician = [m for m in band.members if m.name == musician_name][0]
        except IndexError:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")

        band.members.remove(musician)
        return f"{musician_name} was removed from {band_name}."

    @staticmethod
    def rock_concert(singer: Singer, drummer: Drummer, guitarist: Guitarist):
        if "play the drums with drumsticks" in drummer.skills and "sing high pitch notes" in singer.skills \
                                                                        and "play rock" in guitarist.skills:
            return True
        return False

    @staticmethod
    def metal_concert(singer: Singer, drummer: Drummer, guitarist: Guitarist):
        if "play the drums with drumsticks" in drummer.skills and "sing low pitch notes" in singer.skills \
                and "play metal" in guitarist.skills:
            return True
        return False

    @staticmethod
    def jazz_concert(singer: Singer, drummer: Drummer, guitarist: Guitarist):
        if "play the drums with drum brushes" in drummer.skills and \
                ("sing high pitch notes" and "sing low pitch notes" in singer.skills) \
                and "play jazz" in guitarist.skills:
            return True
        return False

    def start_concert(self, concert_place: str, band_name: str):
        band = [b for b in self.bands if b.name == band_name][0]
        concert = [c for c in self.concerts if c.place == concert_place][0]

        try:
            singer = [s for s in band.members if type(s) == Singer][0]
            drummer = [d for d in band.members if type(d) == Drummer][0]
            guitarist = [g for g in band.members if type(g) == Guitarist][0]
        except IndexError:
            raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

        if concert.genre == "Rock":
            if not self.rock_concert(singer, drummer, guitarist):
                raise Exception(f"The {band_name} band is not ready to play at the concert!")
        elif concert.genre == "Metal":
            if not self.metal_concert(singer, drummer, guitarist):
                raise Exception(f"The {band_name} band is not ready to play at the concert!")
        elif concert.genre == "Jazz":
            if not self.jazz_concert(singer, drummer, guitarist):
                raise Exception(f"The {band_name} band is not ready to play at the concert!")

        profit = (concert.audience * concert.ticket_price) - concert.expenses
        return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert_place}."
