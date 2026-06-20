import pytest
from solution import Solution

class TestProductExceptSelf:
    
    @pytest.fixture(autouse=True)
    def setup(self):
        self.solver = Solution()

    @pytest.mark.parametrize("nums, expected", [
        # --- Standard LeetCode Examples ---
        ([1, 2, 4, 6], [48, 24, 12, 8]),
        ([-1, 0, 1, 2, 3], [0, -6, 0, 0, 0]),
        
        # --- Zero Edge Cases (Critical for this problem) ---
        ([0, 0], [0, 0]),                               # Multiple zeros
        ([1, 2, 0, 4, 0], [0, 0, 0, 0, 0]),             # Multiple zeros dispersed
        ([0, 5, 2, -1], [-10, 0, 0, 0]),                # Single zero at the start
        ([4, 2, 3, 0], [0, 0, 0, 24]),                  # Single zero at the end
        
        # --- Negative and Minimum Length Cases ---
        ([2, 3], [3, 2]),                               # Minimum length constraint
        ([-2, -3], [-3, -2]),                           # Minimum length with negatives
        ([-1, -2, -3, -4], [-24, -12, -8, -6]),         # All negative numbers
        ([-1, 2, -3, 4], [-24, 12, -8, 6]),             # Alternating signs
        
        # --- Value Variations ---
        ([1, 1, 1, 1, 1], [1, 1, 1, 1, 1]),             # All identical (ones)
        ([-1, -1, -1, -1], [-1, -1, -1, -1]),           # All identical (negative ones)
        ([20, 1, 1, 1], [1, 20, 20, 20])                # One large number, rest small
    ])
    def test_productExceptSelf(self, nums, expected):
        assert self.solver.productExceptSelf(nums) == expected

    # --- Isolated Constraint Edge Cases ---
    
    def test_productExceptSelf_max_length(self):
        # We use an array of 1s and -1s to ensure the product doesn't exceed 
        # the 32-bit integer constraint mathematically guaranteed by the problem.
        nums = [1 if i % 2 == 0 else -1 for i in range(1000)]
        
        # The product of all other elements will alternate between 1 and -1
        # depending on which element is being excluded.
        # Total array has 500 '1's and 500 '-1's.
        # Excluding a '1' leaves 500 '-1's (even) -> product is 1
        # Excluding a '-1' leaves 499 '-1's (odd) -> product is -1
        expected = [1 if i % 2 == 0 else -1 for i in range(1000)]
        
        assert self.solver.productExceptSelf(nums) == expected