from lib.game import *
from lib.simulation import Simulation

a = Simulation(NeverChangeGame, 10000)
b = Simulation(RandomChangeGame, 10000)
c = Simulation(AlwaysChangeGame, 10000)

print(a.statistics)
print(b.statistics)
print(c.statistics)
