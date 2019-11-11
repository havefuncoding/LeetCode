class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Dictionary to hold unfulfilled to-be complements, num:idx
        d = {}
        
        # Iterate through each number in array
        for idx,current in enumerate(nums):
            # If number's complement in dictionary
            complement = target - current
            if complement in d:
                # Then return complement's index from dictionary with the current number index
                return [d[complement], idx]            
            # Else insert this num:idx to the dictionary to be picked up as another number's complement
            else:
                d[current] = idx
        
        # If no complements matched, return empty
        return []
        
