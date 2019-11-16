class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """    
        # Return s as-is if numRows == 1 or numRows >= len(s)
        if numRows == 1 or numRows >= len(s):
            return s
        
        # Initialize array with numRows count of empty strings
        rows = [''] * numRows
        
        # Row and col both start at 0, with row_direction going up
        # Row goes up until last row, then goes down until 1st row, on and on
        # Col stays same while row goes up, goes right +1 only while row goes up
        row = 0
        #col = 0      
        row_direction = 1
        
        # Go through each char in string
        for char in s:
            rows[row] += char
            if row == numRows - 1:
                row_direction = -1
            elif row == 0:
                row_direction = 1
            row += row_direction
            
        return ''.join(rows)
