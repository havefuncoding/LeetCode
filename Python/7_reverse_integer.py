class Solution:
    def reverse(self, x: int) -> int:
        sign = 1                        # Sign initialized to positive
        
        if x < 0:                       # If x less than 0
            sign = -1                   # Update sign to negative
            x *= -1                     # Update x to positive so that we can use while x > 0 condition
        
        res = 0                         # Build res from 0
        
        while x > 0:                    # While digits remaining in x
            res = res * 10 + x % 10     # Add last digit to the back of res
            x //= 10                    # Remove last digit of x
            
        return res * sign               # Return res updated with correct staring sign
    
        
