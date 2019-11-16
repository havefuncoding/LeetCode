class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Initialize empty array to collect trios that sum to 0
        # Return immediately if input size is less than 3, insufficient for trio
        result = []
        if len(nums) < 3:
            return result
        
        # Otherwise sort from smallest to largest number
        nums.sort()
        
        # And iterate from 1st to 3rd-to-last number (so that we have 3 elements from position)
        for current in range(len(nums) - 2):    # current is whatever is being iterated 
            # If current happens to be a repeat of previous current
            # Then skip, bc we already explored this route
            if current > 0 and nums[current] == nums[current - 1]:
                continue
            
            # Otherwise start left just after current, and start right at the end
            left = current + 1
            right = len(nums) - 1
            
            # And explore all possible combinations with rest of list
            # Ensuring none is overlapped/repeated by checking left < right
            while (left < right):
                
                # Check the trio sum
                sum_of_trio = nums[current] + nums[left] + nums[right]

                # If trio sum too little, then move left rightward, to larger number
                if sum_of_trio < 0:
                    left += 1
                
                # If trio sum too much, then move right leftward, to smaller number
                elif sum_of_trio > 0:
                    right -= 1
                
                # If trio sum is perfect, then ...
                else:
                    result.append([nums[current], nums[left], nums[right]]) # add trio to result
                    left +=1                                                # move left, rightward
                    right -= 1                                              # move right, leftward
                
                    while left < right and nums[left] == nums[left-1]:      # and skip any repeats
                        left += 1                                           # as long as left of right
                        
                    while right > left and nums[right] == nums[right+1]:    # also skip right
                        right -= 1                                          # as long as right of left
            
        return result
