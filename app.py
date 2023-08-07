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


starting_wealth = 100.0
players = 10000
rounds = 1
expected_1 = 0.5 * (starting_wealth * WIN + starting_wealth * LOSE)

wallets = simulate(starting_wealth, players, rounds)
average = mean(wallets)

print("lim players -> inf")
print(f"expected -> {expected_1}")
print(f"mean(simulate({starting_wealth}, {players}, {rounds})) = {average}")
