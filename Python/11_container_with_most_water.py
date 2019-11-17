# https://leetcode.com/problems/container-with-most-water/
class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        #height = [1,8,6,2,5,4,8,3,7]

        res = 0                     # Track only largest area
        left = 0                    # Start 1st wall, work rightwards
        right = len(height) - 1     # Start last wall, work leftwards

        while left < right:         # While left wall is left of right wall
            #print(f"\n\n----- res({res}) l({left}) r({right}) -----\t", end="")
            shorter = min(height[left], height[right])  # Take shorter of the 2 walls
            distance = right - left                     # Calc distance between 2 walls
            res = max(res, shorter * distance)          # Calc area, shorter * distance
            left = left + (height[left] == shorter)     # Move shorter of the 2 inwards
            right = right - (height[right] == shorter)  # ...either left or right wall
            #print(f"sh({shorter}) d({distance}) l({left}) r({right})")

        return res
