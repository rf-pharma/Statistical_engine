import random

def simulate_crashes(days, prob=0.045):
    crashes = sum(1 for _ in range(days) if random.random() < prob)
    return crashes / days

if __name__ == "__main__":
    for d in [30, 365, 10000]:
        print(d, simulate_crashes(d))
