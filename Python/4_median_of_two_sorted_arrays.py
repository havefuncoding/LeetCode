class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """  
        combined = sorted(nums1 + nums2)    # Combine and sort the 2 lists
        
        length = len(combined)              # Get the length of the combined list
        midpoint = length // 2              # Get the midpoint index position
        
        if length % 2 != 0:                 # If odd number of elements
            return combined[midpoint]       # Return the element at midpoint in combined list
        
        else:                               # Otherwise return the avg of the mid 2 elements
            return (combined[midpoint] + combined[midpoint-1]) / 2 
        
       
