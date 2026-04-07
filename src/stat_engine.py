import math
from collections import Counter

class StatEngine:
    def __init__(self, data):
        self.data = [x for x in data if isinstance(x, (int, float))]

        if len(self.data) == 0:
            raise ValueError("Empty dataset")

    def get_mean(self):
        return sum(self.data) / len(self.data)

    def get_median(self):
        s = sorted(self.data)
        n = len(s)
        mid = n // 2
        return (s[mid] + s[~mid]) / 2

    def get_mode(self):
        freq = Counter(self.data)
        max_count = max(freq.values())
        return [k for k, v in freq.items() if v == max_count]

    def get_variance(self, sample=True):
        mean = self.get_mean()
        n = len(self.data)
        denom = n - 1 if sample else n
        return sum((x - mean) ** 2 for x in self.data) / denom

    def get_std(self, sample=True):
        return math.sqrt(self.get_variance(sample))

    def get_outliers(self, threshold=2):
        mean = self.get_mean()
        std = self.get_std()
        return [x for x in self.data if abs(x - mean) > threshold * std]
