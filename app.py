import random
from statistics import mean

WIN_REWARD = 0.5
LOSE_COST = 0.4
WIN = 1 + WIN_REWARD
LOSE = 1 - LOSE_COST


def simulate(starting_wealth, players, rounds):
    wallets = [starting_wealth] * players

    for r in range(rounds):
        for p in range(players):
            if random.choice([0, 1]):
                wallets[p] *= WIN
            else:
                wallets[p] *= LOSE

    return wallets


STARTING_WEALTH = 100.0
PLAYERS = 10000
ROUNDS = 1


wallets = simulate(STARTING_WEALTH, PLAYERS, ROUNDS)
average = mean(wallets)

# lim PLAYERS -> inf,
# mean(wallets) -> 0.5 * (STARTING_WEALTH * WIN + STARTING_WEALTH * LOSE)
print(f"mean(simulate({STARTING_WEALTH}, {PLAYERS}, {ROUNDS})) = {average}")
# mean(simulate(100.0, 10000, 1)) = 104.64
