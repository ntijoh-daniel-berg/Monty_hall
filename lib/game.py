from lib.door import Door
import random


class Game(object):

    def __init__(self):
        self.doors = [Door(secret='goat'),
                      Door(secret='goat'),
                      Door(secret='car')]
        random.shuffle(self.doors)
        self.picked_door = self.doors[random.randint(0, 2)]
        self.picked_door.pick()
        self.reveal_goat()
        self.play()

    def play(self):
        raise NotImplementedError

    def reveal_goat(self):
        for i, door in enumerate(self.doors):
            if not door.is_picked and not door.is_car:
                self.doors.pop(i)
                break

    def is_won(self):
        return self.picked_door.is_car


class NeverChangeGame(Game):

    def play(self):
        pass


class RandomChangeGame(Game):

    def play(self):
        self.picked_door = self.doors[random.randint(0, 1)]


class AlwaysChangeGame(Game):

    def play(self):
        for door in self.doors:
            if not door.is_picked:
                self.picked_door = door
                break
