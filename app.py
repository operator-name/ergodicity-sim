import random
from statistics import mean, median, log

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


def print_stats(wallets, lim_str):
    avg = mean(wallets)
    exp_avg = starting_wealth * ((0.5 * (WIN + LOSE)) ** rounds)

    med = median(wallets)
    winners = len([w for w in wallets if w > starting_wealth])
    big_losers = len([w for w in wallets if w > (0.1 * starting_wealth)])

    print(f"{starting_wealth=:,}, {players=:,}, {rounds=:,}")
    print(f"mean = {avg:.2f}")
    print(lim_str)
    print(f"expected mean -> {exp_avg:.2f}")
    print(f"median = {med:.2f}")
    print(f"wallets > {starting_wealth:,} = {winners/players:.2%}")
    print(f"wallets < {0.1 * starting_wealth:,} = {big_losers/players:.2%}")
    print(f"{max(wallets)=:.2f}, {min(wallets)=:.2f}")


starting_wealth = 100.0
players = 100000
rounds = 1

wallets_1 = simulate(starting_wealth, players, rounds)
print_stats(wallets_1, "lim players -> inf")
print()

starting_wealth = 100.0
players = 100000
rounds = 10

wallets_n = simulate(starting_wealth, players, rounds)
print_stats(wallets_n, "lim players -> inf")
print()

starting_wealth = 1_000_000.0
players = 500
rounds = 10000

wallets_t = simulate(starting_wealth, players, rounds)
print_stats(wallets_t, "lim rounds -> inf")
wallets_log_t = [log(w) for w in wallets_t]
print(f"mean(log) = {mean(wallets_log_t)}")
print()
