import random
from statistics import mean, median

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

wallets = simulate(starting_wealth, players, rounds)
avg = mean(wallets)
exp_avg = starting_wealth * ((0.5 * (WIN + LOSE)) ** rounds)

med = median(wallets)
winners = len([w for w in wallets if w > starting_wealth])
big_losers = len([w for w in wallets if w > (0.1 * starting_wealth)])

print(f"{starting_wealth=}, {players=}, {rounds=}")
print(f"mean = {avg}")
print("lim players -> inf")
print(f"{rounds=}")
print(f"expected mean -> {exp_avg}")
print()
print(f"median = {med}")
print(f"wallets > starting_wealth = {winners/players:.0%}")
print(f"wallets < 0.1 * starting_wealth = {big_losers/players:.0%}")
print(f"{max(wallets)=}, {min(wallets)=}")

print()
print()

rounds = 10

wallets = simulate(starting_wealth, players, rounds)
avg = mean(wallets)
exp_avg = starting_wealth * ((0.5 * (WIN + LOSE)) ** rounds)

med = median(wallets)
winners = len([w for w in wallets if w > starting_wealth])
big_losers = len([w for w in wallets if w > (0.1 * starting_wealth)])

print(f"{starting_wealth=}, {players=}, {rounds=}")
print(f"mean = {avg}")
print(f"{rounds=}")
print("lim players -> inf")
print(f"expected mean -> {exp_avg}")
print()
print(f"median = {med}")
print(f"wallets > starting_wealth = {winners/players:.0%}")
print(f"wallets < 0.1 * starting_wealth = {big_losers/players:.0%}")
print(f"{max(wallets)=}, {min(wallets)=}")

print()
print()
