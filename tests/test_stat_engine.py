import unittest
from src.stat_engine import StatEngine

class TestStatEngine(unittest.TestCase):

    def test_mean(self):
        self.assertEqual(StatEngine([1,2,3]).get_mean(), 2)

    def test_median(self):
        self.assertEqual(StatEngine([1,2,3,4]).get_median(), 2.5)

    def test_variance(self):
        self.assertAlmostEqual(StatEngine([1,2,3]).get_variance(), 1)

    def test_outliers(self):
        self.assertIn(100, StatEngine([1,2,3,100]).get_outliers())

if __name__ == "__main__":
    unittest.main()
