from lib.game import Game

wins = 0
for i in range(10000):
    game = Game(strategy='never_change')
    if game.is_won():
        wins += 1

print wins

