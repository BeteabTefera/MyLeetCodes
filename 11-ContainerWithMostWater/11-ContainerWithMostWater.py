# Last updated: 8/18/2026, 2:50:59 PM
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
    
        l = 0
        r = len(height) - 1
        area = 0
        while (l < r):
            # l = 1
            # r = 8
            area = max(area, min(height[l], height[r]) * (r - l))
            left_area = min(height[l + 1], height[r]) * (r - (l + 1))
            right_area = min(height[l], height[r - 1]) * (r - 1 - l)
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return area