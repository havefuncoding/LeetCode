class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        
        # Return empty if strs empty, or first str if alone
        if len(strs) == 0: return res
        if len(strs) == 1: return strs[0]
        
        # Get the shortest string in strs
        length = self.shortestLength(strs)
        
        # Check if chars are shared, only up to length of shortest string
        for i in range(length):
            must_share = strs[0][i]         # Use string char at i index as base case
            for s in strs[1:]:              # Check base against remaining strings at same index
                if s[i] != must_share:      # If not equal, then no need to continue
                    return res              
            res += must_share               # Add char if shared across all strings at same index
        return res                          # Return shared chars                    
        
        
    def shortestLength(self, strs):
        res = len(strs[0])                  # Take first string length as base
                                            # If length < 2, it won't even reach here
        for str in strs[1:]:
            if len(str) < res:              # Update if length < res
                res = len(str)
        
        return res                          # Return length of shortest string
