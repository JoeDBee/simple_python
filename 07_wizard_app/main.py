import random
import time

from actors import Creature, Wizard, SmallAnimal, Dragon


def main():
    print_header()
    game_loop()


def print_header():
    print('---------------------------')
    print('      Wizard Game App!     ')
    print('---------------------------')


def game_loop():

    creatures = [
        SmallAnimal('Toad', 1),
        Creature('Tiger', 12),
        SmallAnimal('Bat', 3),
        Dragon('Dragon', 50, 30, True),
        Wizard('Evil Wizard', 100)
    ]

    hero = Wizard('Gandalf', 75)

    while True:

        active_creature = random.choice(creatures)
        print('A {} of level {} has appeared from a dark and spooky forest... \n'
              .format(active_creature.name, active_creature.level))

        cmd = input('Do you [a]ttack, [r]unaway, or [l]ook?')
        cmd = cmd.lower().strip()

        if cmd == 'a':
            if hero.attack(active_creature):
                creatures.remove(active_creature)
            else:
                print("The wizard runs and hides taking time to recover...")
                time.sleep(3)
                print("The wizard returns revitalized!")

        elif cmd == 'r':
            print('The wizard runs away!')

        elif cmd == 'l':
            print('The wizard {} looks around and sees:'.format(hero.name))
            for creature in creatures:
                print(' * A {} of level {}'.
                      format(creature.name, creature.level)
                      )
        else:
            print('Exiting game...')
            break

        if not creatures:
            print('All creatures have been defeated!\n Exiting game...')
            break

        print()


if __name__ == '__main__':
    main()
