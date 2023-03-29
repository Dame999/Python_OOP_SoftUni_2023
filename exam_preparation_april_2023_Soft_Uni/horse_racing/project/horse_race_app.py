from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:
    def __init__(self):
        self.horses: list = []
        self.jockeys: list = []
        self.horse_races: list = []

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        if horse_name in [h.name for h in self.horses]:
            raise Exception(f"Horse {horse_name} has been already added!")

        if horse_type == "Appaloosa":
            self.horses.append(Appaloosa(horse_name, horse_speed))

        elif horse_type == "Thoroughbred":
            self.horses.append(Thoroughbred(horse_name, horse_speed))

        return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        if jockey_name in [j.name for j in self.jockeys]:
            raise Exception(f"Jockey {jockey_name} has been already added!")

        self.jockeys.append(Jockey(jockey_name, age))
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        if race_type in [horse_race.race_type for horse_race in self.horse_races]:
            raise Exception(f"Race {race_type} has been already created!")

        self.horse_races.append(HorseRace(race_type))
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        try:
            jockey = [j for j in self.jockeys if jockey_name == j.name][0]
        except IndexError:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        if horse_type in [horse.__class__.__name__ for horse in self.horses]:
            horses = [horse for horse in self.horses if not horse.is_taken and horse_type == horse.__class__.__name__]
            if horses and jockey.horse is not None:
                return f"Jockey {jockey_name} already has a horse."
        else:
            raise Exception(f"Horse breed {horse_type} could not be found!")

        horse = horses[-1]
        horse.is_taken = True
        jockey.horse = horse

        return f"Jockey {jockey_name} will ride the horse {horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        if race_type not in [hr.race_type for hr in self.horse_races]:
            raise Exception("Race {race_type} could not be found!")

        horse_race = [h for h in self.horse_races if race_type == h.race_type][0]

        if jockey_name not in [j.name for j in self.jockeys]:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        jockey = [j for j in self.jockeys if jockey_name == j.name][0]

        if jockey.horse is None:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        if jockey in horse_race.jockeys:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."

        horse_race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        if race_type not in [race.race_type for race in self.horse_races]:
            raise Exception(f"Race {race_type} could not be found!")

        horse_race = [h for h in self.horse_races if race_type == h.race_type][0]

        if len(horse_race.jockeys) < 2:
            raise Exception("Horse race {race_type} needs at least two participants!")

        winning_jockey = horse_race.jockeys[0]

        for jockey in horse_race.jockeys:
            if jockey.horse.speed > winning_jockey.horse.speed:
                winning_jockey = jockey

        return f"The winner of the {race_type} race, " \
               f"with a speed of {winning_jockey.horse.speed}km/h is {winning_jockey.name}! " \
               f"Winner's horse: {winning_jockey.horse.name}."









