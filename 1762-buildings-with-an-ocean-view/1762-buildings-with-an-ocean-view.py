class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        n = len(heights)
        res = []
        maxh = 0
        
        for i in range(n - 1, -1, -1):
            if heights[i] > maxh:
                res.append(i)
                maxh = heights[i]
                
        return res[::-1]
        
                
                