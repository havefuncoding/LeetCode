class Solution:
    def twoSum(self, nums, target):
        """
        type nums: List[int]
        type target: int
        rtype: List[int]
        """
        d = {}
        for i in range(len(nums)):
            current_num = nums[i]
            current_nums_complement = target - current_num
            
            # If the current number's complement is already in dictionary
            if current_nums_complement in d:
                
                # Then return complement's index and current number's index
                return [d[current_nums_complement], i]
                
            # Else add to dictionary, current number:index
            d[current_num] = i
            

"""Test"""
tests = [
            [[3,2,4], 6],
            [[2,7,11,15], 9]
        ]

solution = Solution()
for test in tests:
    print(solution.twoSum(test[0], test[1]), end="")
    print(f"\t:\tnums={test[0]}, target={test[1]}")

"""Reference
$ python 1_two_sum.py
[1, 2]	:	nums=[3, 2, 4], target=6
[0, 1]	:	nums=[2, 7, 11, 15], target=9
"""
