import pytest
from solution import Solution

class TestTwoSum:
    
    @pytest.fixture(autouse=True)
    def setup(self):
        self.solver = Solution()

    @pytest.mark.parametrize("nums, target, expected", [
        # --- Standard LeetCode Examples ---
        ([3, 4, 5, 6], 7, [0, 1]),
        ([4, 5, 6], 10, [0, 2]),
        ([5, 5], 10, [0, 1]),
        
        # --- Negative and Mixed Value Cases ---
        ([-1, -2, -3, -4, -5], -8, [2, 4]),               # All negatives
        ([-10, 7, 19, 15], 9, [0, 2]),                    # Mixed signs
        ([0, 4, 3, 0], 0, [0, 3]),                        # Zeroes involved
        
        # --- Structural Edge Cases ---
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 19, [8, 9]),    # Target pair at the very end
        ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 19, [0, 1]),    # Target pair at the very beginning
        ([2, 7, 11, 15, 27], 38, [2, 4]),                 # Dispersed pair
        
        # --- Value Extreme Constraints (+/- 10,000,000) ---
        ([10000000, 5, 10000000], 20000000, [0, 2]),      # Max positive constraints
        ([-10000000, 5, -10000000], -20000000, [0, 2]),   # Min negative constraints
        ([-10000000, 10000000], 0, [0, 1])                # Min and Max combined
    ])
    def test_twoSum(self, nums, target, expected):
        assert self.solver.twoSum(nums, target) == expected

    # --- Isolated Constraint Edge Cases ---
    # We test the maximum length constraint (1000 elements) in an isolated 
    # function to keep terminal output clean and prevent buffer overflow.
    def test_twoSum_max_length(self):
        # Create an array of 998 ones, followed by 2 and 3. Target is 5.
        nums = [1] * 998 + [2, 3]
        target = 5
        
        # The elements 2 and 3 are at the very end (indices 998 and 999)
        assert self.solver.twoSum(nums, target) == [998, 999]