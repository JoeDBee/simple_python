import random


class Creature:
    def __init__(self, name, level):
        #  self.X = Y
        # ie X and Y don't need to be exactly the same
        self.name = name
        self.level = level

    # representation - useful for debugging
    def __repr__(self):
        return "Creature {} of level {}". format(
            self.name, self.level
        )

    def get_defensive_roll(self):
        return random.randint(1, 20) * self.level


# Inherited classes need to be defined after main class
class Wizard(Creature):
    # We can use the init method along with super()
    # if we want to add more to the wizard init
    # def __init__(self, name, level):
    #     super().__init__(name, level)

    def attack(self, creature):
        print("The wizard {} attacks {}\n". format(
            self.name, creature.name
        ))

        hero_roll = self.get_defensive_roll()
        creature_roll = self.get_defensive_roll()

        print("{} rolls {}...".format(self.name, hero_roll))
        print("{} rolls {}...\n".format(creature.name, creature_roll))

        if hero_roll >= creature_roll:
            print("{} has triumphed over {}".format(self.name, creature.name))
            return True
        else:
            print("{} has been defeated by {}".format(self.name, creature.name))
            return False


class SmallAnimal(Creature):
    # we can redefine this function for the inherited method
    # without/without the super builtin
    def get_defensive_roll(self):
        # base_roll = random.randint(1, 20) * self.level
        base_roll = super().get_defensive_roll()
        return base_roll * 0.5


class Dragon(Creature):
    def __init__(self, name, level, scaliness, breaths_fire):
        super().__init__(name, level)
        self.fire = breaths_fire
        self.scaliness = scaliness

    def get_defensive_roll(self):
        base_roll = super().get_defensive_roll()
        fire_mod = 5 if self.fire else 1
        scale_mod = self.scaliness / 10
        return base_roll * fire_mod * scale_mod
