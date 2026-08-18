from typing import List

class Solution:
    
    def maxArea(self, height: List[int]) -> int:
        left = 0 
        right = len(height) - 1
        maxArea = 0
        
        while left < right:
            width = right - left
            water_height = min(height[left], height[right])
            area = width * water_height
        
            maxArea = max(maxArea, area)
        
            #move the shorter wall
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
            return maxArea
        
if __name__ == '__main__':
    Sol = Solution()
    print(Sol.maxArea([3,5,6,1,3,7,3]))