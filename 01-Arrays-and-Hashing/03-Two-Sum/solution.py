
"""
Problem: Two Sum
Link: https://leetcode.com/problems/two-sum/
Approach: One-pass Hash Map. Store elements and their indices as we iterate. 
For each element, check if the complement (target - element) exists in the map.
Time Complexity: O(n)
Space Complexity: O(n)
"""
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Dictionary to store value : index
        prev_map = {} 
        
        for i, num in enumerate(nums):
            diff = target - num
            
            # If the complement exists in our map, we found the pair
            if diff in prev_map:
                return [prev_map[diff], i]
                
            # Otherwise, add the current number and its index to the map
            prev_map[num] = i
            
        # The problem guarantees exactly one valid answer, 
        # so this return is technically unreachable with valid inputs.
        return []