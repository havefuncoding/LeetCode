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
            
            if curr > 0 and nums[curr] == nums[curr-1]:             # Skip if a repeat
                continue              
            left = curr + 1                                         # Define start
            right = input_size -1
            
            print(f"\n\n----- {curr} {left} {right} ------", end="")
        
            while left < right:
                this_sum = nums[curr] + nums[left] + nums[right]    # Get sum
                this_prox = abs(this_sum - target)                  # Get proximity
                
                print(f"\tres({this_sum}) prox({this_prox})", end="\t-> ")
                
                if this_prox < res_prox:                            # Compare proximity
                    res_sum = this_sum                              # Update if closer
                    res_prox = this_prox
                left += 1                                     
                right -= 1
                
                print(f"\tres({res_sum}) prox({res_prox})", end="\t")

                while left < right and nums[left] == nums[left-1]:
                    left += 1                                       # Skip repeats
                while left < right and nums[right] == nums[right+1]:
                    right -= 1                                      # Skip repeats
                   
                print(f"l({left}), r({right})")
                
        return res_sum
