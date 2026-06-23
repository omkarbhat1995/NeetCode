import unittest
from solution import Solution

class TestTrappingRainWater(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    # --- Base Cases ---
    def test_example_1(self):
        heights = [0,2,0,3,1,0,1,3,2,1]
        self.assertEqual(self.solution.trap(heights), 9)

    def test_leetcode_classic(self):
        heights = [0,1,0,2,1,0,1,3,2,1,2,1]
        self.assertEqual(self.solution.trap(heights), 6)

    # --- Edge Cases ---
    def test_minimum_length(self):
        # Constraints specify 1 <= height.length
        self.assertEqual(self.solution.trap([5]), 0)

    def test_two_elements(self):
        # Need at least 3 elements to trap water
        self.assertEqual(self.solution.trap([5, 5]), 0)

    def test_all_zeros(self):
        # Flat land, no elevation
        self.assertEqual(self.solution.trap([0, 0, 0, 0, 0]), 0)

    def test_flat_elevation(self):
        # Flat land, high elevation
        self.assertEqual(self.solution.trap([5, 5, 5, 5, 5]), 0)

    def test_strictly_increasing(self):
        # Water just runs off
        self.assertEqual(self.solution.trap([1, 2, 3, 4, 5]), 0)

    def test_strictly_decreasing(self):
        # Water just runs off
        self.assertEqual(self.solution.trap([5, 4, 3, 2, 1]), 0)

    def test_single_bowl(self):
        # A simple trap in the middle
        self.assertEqual(self.solution.trap([5, 0, 5]), 5)

    def test_wide_bowl(self):
        # A wide trap
        self.assertEqual(self.solution.trap([5, 0, 0, 0, 5]), 15)

    def test_v_shape_valley(self):
        # Valley trap
        heights = [10, 9, 8, 7, 6, 5, 6, 7, 8, 9, 10]
        # Max water is bounded by 10 on both sides.
        # Trapped per column: 0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0 -> Total = 25
        self.assertEqual(self.solution.trap(heights), 25)

    def test_mountain_shape(self):
        # Peak in the middle, water runs off both sides
        heights = [1, 2, 3, 5, 3, 2, 1]
        self.assertEqual(self.solution.trap(heights), 0)

    def test_multiple_identical_bowls(self):
        # Repeated pattern
        self.assertEqual(self.solution.trap([5, 1, 5, 1, 5, 1, 5]), 12) # 4+4+4 = 12

    def test_extreme_height_differences(self):
        # Max constraint values
        self.assertEqual(self.solution.trap([1000, 0, 1000]), 1000)

    def test_large_number_of_small_traps(self):
        # Alternating heights
        heights = [2, 1] * 500  # Length 1000
        # The last element will be 1. Bounded by 2.
        # It creates 499 traps of depth 1.
        self.assertEqual(self.solution.trap(heights), 499)

if __name__ == '__main__':
    unittest.main()