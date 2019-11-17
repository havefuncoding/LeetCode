# https://leetcode.com/problems/3sum-closest/submissions/
class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # Get the starter conditions out of the way, if empty, if only 3 elements
        input_size = len(nums)
        if input_size == 0: return 0
        if input_size == 3: return sum(nums)
        
        res_sum = 0                             # Track sum closest to target
        res_prox = 2**31 - 1                    # Track proximity to target
        nums.sort()                             # Sort nums from smallest to largest
    
        for curr in range(input_size - 2):      # Iterate 1st to 3rd-to-last trios
            
            if curr > 0 and nums[curr] == nums[curr-1]: # Skip if a repeat
                continue              
            left = curr + 1                     # Start left just after current    
            right = input_size -1               # Start right at the end
            
            while left < right:                 # While left < right
                this_sum = nums[curr] + nums[left] + nums[right]    # Get sum 
                
                #print(f"\nsum({this_sum})\t{nums}\tc({nums[curr]}) l({nums[left]}) r({nums[right]})\n")
                
                this_prox = abs(this_sum - target)                  # Get proximity
                
                if this_prox < res_prox:                            # Compare and update if closer
                    res_sum = this_sum                              
                    res_prox = this_prox
                
                if this_sum < target:                               # Move right if sum < target
                    left += 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1                                   # Skipping repeats
                    
                elif this_sum > target:                             # Move left is sum > target
                    right -= 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1                                  # Skipping repeats
                    
                else:                                               # If sum == target, done.
                    return res_sum                                  # Either res_sum or this_sum

        return res_sum
