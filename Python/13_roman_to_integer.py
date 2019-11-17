class Solution:
    def romanToInt(self, s: str) -> int:
        """
        Input: "LVIII"
        Output: 58
        Explanation: L = 50, V= 5, III = 3.
        """
        res = 0
        
        for i, c in enumerate(s):
            add = 0
            
            # Add literal value if char is 'I' or char previous is not relevant
            # Else add updated value minus value already added with last valu
            # So if 'I'added 1 previously, following 'V' adds 3, which is 4 minus last added
            # Such that 'IV' is 4
            if c == 'I': add = 1  
            elif c == 'V':
                add = add + 3 if (i > 0 and s[i-1] == 'I') else add + 5   
            elif c == 'X':
                add = add + 8 if (i > 0 and s[i-1] == 'I') else add + 10      
            elif c == 'L':
                add = add + 30 if (i > 0 and s[i-1] == 'X') else add + 50
            elif c == 'C':
                add = add + 80 if (i > 0 and s[i-1] == 'X') else add + 100
            elif c == 'D':
                add = add + 300 if (i > 0 and s[i-1] == 'C') else add + 500
            elif c == 'M':
                add = add + 800 if (i > 0 and s[i-1] == 'C') else add + 1000
            
            res += add
            #print(f"i={i}, c={c}, add={add}, res={res}")
            
        return res

    def romanToInt(self, s):
        """
        Input: "LVIII"
        Output: 58
        Explanation: L = 50, V= 5, III = 3.
        """
        values = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        prev = 0
        total = 0
        
        for c in s[::-1]:       # Iterate chars from right to left, from smallest
            curr = values[c]       
            
            if curr < prev:     # Subtract if current is smaller than previous
                total -= curr   
            else:               # Otherwise, nothing to handle, so add as normal
                total += curr   
            
            prev = curr         # Update prev to curr and continue left to next char
        
        return total
