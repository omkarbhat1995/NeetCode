from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Finds the maximum amount of water a container can store.
        
        :param height: List of non-negative integers representing bar heights.
        :return: Integer representing the maximum water area.
        """
        left = 0
        right = len(height) - 1
        max_water = 0
        
        while left < right:
            # The height of the container is limited by the shorter bar
            current_height = min(height[left], height[right])
            # The width is the distance between the two pointers
            current_width = right - left
            
            # Calculate current area and update max_water if it's larger
            current_area = current_height * current_width
            max_water = max(max_water, current_area)
            
            # To maximize area, we should always move the shorter pointer inward 
            # in hopes of finding a taller line further in.
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_water