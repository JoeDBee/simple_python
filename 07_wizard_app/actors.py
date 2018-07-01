import random


class Wizard:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def attack(self, creature):
        print("The wizard {} attacks {}\n". format(
            self.name, creature.name
        ))

        hero_roll = random.randint(1, 20) * self.level
        creature_roll = creature.get_defensive_roll()

        print("{} rolls {}...".format(self.name, hero_roll))
        print("{} rolls {}...\n".format(creature.name, creature_roll))

        if hero_roll >= creature_roll:
            print("{} has triumphed over {}".format(self.name, creature.name))
            return True
        else:
            print("{} has been defeated by {}".format(self.name, creature.name))
            return False


class Creature:
    def __init__(self, name, the_level):
        self.name = name
        self.level = the_level

    def __repr__(self):
        return "Creature {} of level {}". format(
            self.name, self.level
        )

    def get_defensive_roll(self):
        return random.randint(1, 20) * self.level
