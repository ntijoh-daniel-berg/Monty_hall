from lib.door import Door
import random


class Game(object):

    def __init__(self, strategy):
        self.strategy = strategy
        self.doors = [Door(secret='goat'),
                      Door(secret='goat'),
                      Door(secret='car')]
        random.shuffle(self.doors)
        if self.strategy == 'never_change':
            self.picked_door = self.doors[random.randint(0, 2)]
        elif self.strategy == 'random_change':
            pass
        elif self.strategy == 'always_change':
            pass


    def is_won(self):
        return self.picked_door.secret == 'car'