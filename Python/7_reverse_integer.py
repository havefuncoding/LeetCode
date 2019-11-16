class Solution:
    def reverse(self, x: int) -> int:
        # If x is negative, return res * negative one
        sign = -1 if x < 0 else 1
        res = 0
        
        while x > 0:                    # While digits remaining in x
            res = res * 10 + x % 10     # Add last digit to the back of res
            x //= 10                    # Remove last digit of x
            
        return res * sign               # Return res updated with correct staring sign
    
        
