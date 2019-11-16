"""
Input: "42"
Output: 42

Input: "   -42"
Output: -42
Explanation: The first non-whitespace character is '-', which is the minus sign.
             Then take as many numerical digits as possible, which gets 42.

Input: "4193 with words"
Output: 4193
Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.

Input: "words and 987"
Output: 0
Explanation: The first non-whitespace character is 'w', which is not a numerical 
             digit or a +/- sign. Therefore no valid conversion could be performed.

Input: "-91283472332"
Output: -2147483648
Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
             Thefore INT_MIN (−231) is returned.
"""

class Solution:
    def myAtoi(self, str: str) -> int:
        
        is_negative = False                             # Flag if number is negative
        res = 0                                         # Build number with digits from string
        
        i = 0                                           # Start from beginning of string
        last_i = len(str) - 1                           # Until end of string

        while i <= last_i and str[i] == ' ':            # Skip all leading whitespaces
            i += 1

        if i <= last_i and str[i] in ['-', '+']:        # Only allow first/one sign, if any
            if str[i] == '-':       
                is_negative = True                      # Update is_negative if negative sign
            i += 1                  
        
        while i <= last_i and str[i] >= '0' and str[i] <= '9':  
            res = res * 10 + int(str[i])                # Add all digits (only) to res
            i += 1
                                                    
        if is_negative:                                 # Update, if is_negative is True
            res = -(res)
        
        int_max = 2 ** 31 - 1                           # Calculate the int_max
        int_min = -(2 ** 31)                            # ...and int_max

        if res < int_min:                               # Return int_min if res below threshold
            return int_min
        if res > int_max:                               # Return int_max if res above threshold
            return int_max
  
        return res                                      
