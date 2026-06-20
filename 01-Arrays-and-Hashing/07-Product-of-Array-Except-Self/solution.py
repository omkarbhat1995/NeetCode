"""
Problem: Product of Array Except Self
Link: https://leetcode.com/problems/product-of-array-except-self/
Approach: Use a two-pass strategy. Calculate prefix products directly into the 
result array from left to right. Then, calculate postfix products on the fly 
from right to left, multiplying them into the result array.
Time Complexity: O(n)
Space Complexity: O(1) (excluding the output array)
"""
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        
        # Calculate prefix products and store them in the result array
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
            
        # Calculate postfix products and multiply them into the result array
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
            
        return res