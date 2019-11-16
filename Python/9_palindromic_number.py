"""
Input: 121
Output: true

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0:
            return False    # Negative numbers cannot be palindromic because of "-"
        
        copy = x            # Take a copy of x
        copy_reversed = 0   # Build the reversed digits of x
        
        while x > 0:        # Check while x > 0
            copy_reversed = copy_reversed * 10 + x % 10 # Add last digit of x to copy_reversed
            x //= 10        # And update/remove last digit from x
            
        return copy == copy_reversed    # Return whether or not nums are equivalent after reversing digits
            
