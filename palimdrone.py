class Solution:
    def isPalindrome(self, x: int) -> bool:
        xStr = str(x)
        if(len(str(x)) < 2):
            #single char strings are palindromes.
            return True
        
        elif (len(xStr)%2 == 0):
            #isEven
            firstHalf = xStr[0:len(xStr)//2]
            endHalf = xStr[len(xStr)//2:len(xStr)]
            return firstHalf == endHalf[::-1]
            
        else:
            #odd
            firstHalf = xStr[0:len(xStr)//2]
            endHalf = xStr[(len(xStr)//2)+1:len(xStr)]
            return firstHalf == endHalf[::-1]
            
    def isPalindromeNumber(self, x: int) -> bool:
        # Negative numbers aren't palindromes.
        # A number ending in 0 can't be one unless it is 0.
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_half = 0

        while x > reversed_half:
            digit = x % 10
            reversed_half = reversed_half * 10 + digit
            x //= 10

        # Even digits: 1221 -> 12 == 12
        # Odd digits: 12321 -> 12 == 123 // 10
        return x == reversed_half or x == reversed_half // 10
    
    
    
    
    
    
if __name__ == '__main__':
    sol = Solution()
    if (sol.isPalindromeNumber(5655565)):
        print( "True" )
    else:
        print( "False" )