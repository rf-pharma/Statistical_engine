from src.stat_engine import StatEngine

data = [10, 20, 30, 40, 1000]

engine = StatEngine(data)

print("Mean:", engine.get_mean())
print("Median:", engine.get_median())
print("Mode:", engine.get_mode())
print("Variance:", engine.get_variance())
print("Std Dev:", engine.get_std())
print("Outliers:", engine.get_outliers())
