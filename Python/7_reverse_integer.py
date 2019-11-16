"""
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""
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

        res *= sign                     # Apply sign on res

        # Need to handle overflow,  [−2^31,  2^31 − 1]
        int_max = 2 ** 31 - 1
        int_min = -(2 ** 31)

        if res < int_min or res > int_max:
            return 0

        return res
