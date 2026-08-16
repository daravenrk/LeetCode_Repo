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
            
    
    
    
    
    
    
    
if __name__ == '__main__':
    sol = Solution()
    if (sol.isPalindrome(5655565)):
        print( "True" )
    else:
        print( "False" )