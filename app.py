import random
from statistics import mean

WIN_REWARD = 0.5
LOSE_COST = 0.4
WIN = 1 + WIN_REWARD
LOSE = 1 - LOSE_COST

STARTING_WEALTH = 100.0
PLAYERS = 10000
ROUNDS = 1

wallets = [STARTING_WEALTH] * PLAYERS

for r in range(ROUNDS):
    for p in range(PLAYERS):
        if random.choice([0, 1]):
            wallets[p] *= WIN
        else:
            wallets[p] *= LOSE

# lim PLAYERS -> inf,
# mean(wallets) -> 0.5 * (STARTING_WEALTH * WIN + STARTING_WEALTH * LOSE)
print(f"{mean(wallets)=}")
# mean(wallets)=104.55
