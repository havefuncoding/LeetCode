class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        sub = []                    # Latest all-adjacent all-unique chars substring 'sub'
        longest = 0                 # Longest is longest len(sub) by the end
        
        for i, c in enumerate(s):   # Iterate each index 'i', char 'c' in string 's'
            if c in sub:            # If char is already in substring
                rm = sub.index(c)   # Then get its index position in substring
                sub = sub[rm+1:]    # And reassign substring to all chars after its position
            
            sub.append(c)           # Always add this iteration's char to substring
            
            if len(sub) > longest:  # If latest substring is longer than longest
                longest = len(sub)  # Then update longest with current value
        
        return longest              # Return the longest substring recorded at the end
        
