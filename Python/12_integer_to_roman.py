class Solution:
    def intToRoman(self, num: int) -> str:
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        numerals = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        
        res = ""
        
        for i, value in enumerate(values):  # Check against every possible value
            numeral = numerals[i]           # Get numeral at corresponding index
            count = num // value            # Calculate how many of this numeral to add
            res += numeral * count          # Then add that amount of numeral to res
            num %= value                    # Update num, remove added part from num
        
        return res                              
