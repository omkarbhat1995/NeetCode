import unittest
from solution import Solution

class TestContainerWithMostWater(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    # --- Original Base Cases ---
    
    def test_example_1(self):
        heights = [1, 7, 2, 5, 4, 7, 3, 6]
        self.assertEqual(self.solution.maxArea(heights), 36)

    def test_example_2(self):
        heights = [2, 2, 2]
        self.assertEqual(self.solution.maxArea(heights), 4)

    def test_increasing_heights(self):
        heights = [1, 2, 3, 4, 5]
        self.assertEqual(self.solution.maxArea(heights), 6) 

    def test_decreasing_heights(self):
        heights = [5, 4, 3, 2, 1]
        self.assertEqual(self.solution.maxArea(heights), 6)

    def test_tall_middle_peaks(self):
        heights = [1, 2, 1000, 1000, 2, 1]
        self.assertEqual(self.solution.maxArea(heights), 1000)

    # --- New Edge Cases ---

    def test_minimum_length(self):
        # Constraint minimum: exactly 2 bars
        heights = [1, 1]
        self.assertEqual(self.solution.maxArea(heights), 1)

    def test_minimum_length_with_zeros(self):
        # Constraint minimum with 0 values
        heights = [0, 0]
        self.assertEqual(self.solution.maxArea(heights), 0)

    def test_all_zeros(self):
        # Flat array of zeros
        heights = [0, 0, 0, 0, 0]
        self.assertEqual(self.solution.maxArea(heights), 0)

    def test_zeros_at_ends(self):
        # Pointers must bypass zeros at the ends to find the inner container
        heights = [0, 10, 10, 0]
        self.assertEqual(self.solution.maxArea(heights), 10)

    def test_flat_array(self):
        # All bars are the same height
        heights = [5, 5, 5, 5, 5]
        # Max area is the outermost bars: 5 * (4 - 0) = 20
        self.assertEqual(self.solution.maxArea(heights), 20)

    def test_narrow_tall_vs_wide_short(self):
        # Outer bars are short but wide (2 * 3 = 6)
        # Inner bars are tall but narrow (50 * 1 = 50)
        # Algorithm must properly evaluate the inner pair as larger
        heights = [2, 50, 50, 2]
        self.assertEqual(self.solution.maxArea(heights), 50)

    def test_wide_short_vs_narrow_tall(self):
        # Outer bars are tall and wide (10 * 6 = 60)
        # Inner bars are short (2 * 1 = 2)
        heights = [10, 2, 2, 2, 2, 2, 10]
        self.assertEqual(self.solution.maxArea(heights), 60)

    def test_alternating_heights(self):
        # Peaks and valleys alternating
        heights = [1, 10, 1, 10, 1]
        # Inner 10s: 10 * 2 = 20
        self.assertEqual(self.solution.maxArea(heights), 20)

    def test_one_dominant_side(self):
        # One massive bar, but area is restricted by the other tiny bars
        heights = [100, 1, 1, 1, 1]
        # Max is 1 * 4 = 4
        self.assertEqual(self.solution.maxArea(heights), 4)

    def test_maximum_constraints(self):
        # Simulating max array size (1000) and max heights (1000)
        # Array of 1000 elements, all of height 1000
        heights = [1000] * 1000
        # Max area: 1000 * 999 = 999000
        self.assertEqual(self.solution.maxArea(heights), 999000)

if __name__ == '__main__':
    unittest.main()