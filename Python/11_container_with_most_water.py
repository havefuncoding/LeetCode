# https://leetcode.com/problems/container-with-most-water/
class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        #height = [1,8,6,2,5,4,8,3,7]

        res = 0
        left = 0
        right = len(height) - 1

        while left < right:
            print(f"\n\n----- res({res}) l({left}) r({right}) -----\t", end="")
            shorter = min(height[left], height[right])
            distance = right - left
            res = max(res, shorter * distance)
            left = left + (height[left] == shorter)
            right = right - (height[right] == shorter)
            #print(f"sh({shorter}) d({distance}) l({left}) r({right})")

        return res
