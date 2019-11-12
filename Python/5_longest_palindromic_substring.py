class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        longest = ""                            # Keep track of longest substring

        for i in range(len(s)):                 # Iterate each char in string using indices
            curr = self.getLongest(s, i, i)     # Get palindrome assuming current char at center
            if len(curr) > len(longest):        # If current is longer than longest
                longest = curr                  # Update longest to current value

            curr = self.getLongest(s, i, i+1)   # Get assuming char is left part of center duo
            if len(curr) > len(longest):        # If this current is longer than last longest   
                longest = curr                  # Update longest to current value
    
        return longest                          # Return ultimate longest


    def getLongest(self, s, left, right):
        """
        :type s: str
        :type i: int
        """
        # Radiate outwards while s[left] == s[right] and s hasn't run out on either end
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        return s[left+1:right]  # Return qualifying slice
                                # If s="cWWu", left=1, right=2, returns s[1:3], "WW"
