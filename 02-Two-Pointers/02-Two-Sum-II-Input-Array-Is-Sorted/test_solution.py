# test_solution.py
import unittest

# Import the function from your solution file
from solution import twoSum

class TestTwoSum(unittest.TestCase):

    def test_01_standard_example(self):
        self.assertEqual(twoSum([1, 2, 3, 4], 3), [1, 2])

    def test_02_classic_leetcode_example(self):
        self.assertEqual(twoSum([2, 7, 11, 15], 9), [1, 2])

    def test_03_middle_elements(self):
        self.assertEqual(twoSum([2, 3, 4], 6), [1, 3])

    def test_04_negative_and_zero(self):
        self.assertEqual(twoSum([-1, 0], -1), [1, 2])

    def test_05_all_negative_numbers(self):
        # -5 + -3 = -8. No other pairs equal -8.
        self.assertEqual(twoSum([-5, -4, -3, -2, -1], -8), [1, 3])

    def test_06_mixed_signs(self):
        # -3 + 2 = -1. 
        self.assertEqual(twoSum([-10, -3, 2, 5, 8], -1), [2, 3])

    def test_07_large_numbers(self):
        # 100 + 400 = 500
        self.assertEqual(twoSum([100, 200, 305, 400], 500), [1, 4])

    def test_08_target_is_zero(self):
        # -2 + 2 = 0
        self.assertEqual(twoSum([-2, 1, 2, 5], 0), [1, 3])

    def test_09_duplicate_values(self):
        # 0 + 0 = 0. Distinct indices required, but values can be same.
        self.assertEqual(twoSum([0, 0, 3, 4], 0), [1, 2])

    def test_10_distant_elements(self):
        # 1 + 25 = 26
        self.assertEqual(twoSum([1, 5, 10, 15, 20, 25], 26), [1, 6])

    def test_11_adjacent_elements_at_end(self):
        # 4 + 5 = 9
        self.assertEqual(twoSum([1, 2, 3, 4, 5], 9), [4, 5])

    def test_12_outermost_elements(self):
        # 2 + 10 = 12
        self.assertEqual(twoSum([2, 5, 6, 9, 10], 12), [1, 5])

    def test_13_same_magnitude_opposite_signs(self):
        # -10 + 10 = 0
        self.assertEqual(twoSum([-10, -5, 1, 2, 10], 0), [1, 5])

    def test_14_minimum_array_length(self):
        # Constraints state min length is 2
        self.assertEqual(twoSum([5, 5], 10), [1, 2])

    def test_15_constraint_boundaries(self):
        # Values can be between -1000 and 1000
        self.assertEqual(twoSum([-1000, 1000], 0), [1, 2])

if __name__ == '__main__':
    unittest.main()