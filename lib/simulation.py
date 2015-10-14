class Simulation(object):

    def __init__(self, GameType, reps):
        self.wins = 0
        self.reps = reps
        self.GameType = GameType
        for i in range(reps):
            game = GameType()
            if game.is_won():
                self.wins += 1

    @property
    def statistics(self):
        return "{0}\nRepetitions: {1}\nWins: {2} ({3}%)\n".\
            format(self.GameType.__name__, self.reps, self.wins, (self.wins / float(self.reps)) * 100 )
