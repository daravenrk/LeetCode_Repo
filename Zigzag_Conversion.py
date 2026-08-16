class Solution:
    def convert(self, s: str, numRows: int) -> str:
        #newS = [s[0], s[numRows +2], s[(numRows*2) +2]]
        
        #Character: P A Y P A L I S H I R I N G
        #Row:       0 1 2 1 0 1 2 1 0 1 2 1 0 1
        
        if numRows == 1 or numRows >= len(s):
            return s
        rows = [""] * numRows
        currentRow = 0
        direction = 1
        
        for char in s:
            rows[currentRow] += char
            
            if currentRow == 0:
                direction = 1
            elif currentRow == numRows-1:
                direction = -1
            
            currentRow += direction
        
        return "".join(rows)

if __name__ == '__main__':
    sol = Solution()
    s = 'PAYPALISHIRING' 
    numRows = 4
    print(sol.convert(s, numRows))