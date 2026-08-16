class Solution:
    def reverse(self, x: int) -> int:
        # example 456
        revInt = 0
        isNeg = False
        if (x < 0):
            x = x * -1
            isNeg = True
        while x > 0:
            # find the remainder of or small int
            num = x % 10
            # now reduce the x int
            if x > 0:
                x = x // 10
                revInt = revInt * 10 + num
    
        if(isNeg):
            revInt = -revInt
        
        # test for overflow before returning
        if revInt < -(2**31) or revInt > 2**31 - 1:
            return 0
        
        return revInt
        
        