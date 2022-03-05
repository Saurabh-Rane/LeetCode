class Solution:
    def trap(self, height: List[int]) -> int:
        maxleft = [0] * len(height)
        maxright = [0] * len(height)
        
        maxcurr = 0
        for h in range(len(height)):
            maxleft[h] = maxcurr
            maxcurr = max(maxcurr, height[h])
        
        maxcurr = 0
        for h in range(len(height) - 1, -1, -1):
            maxright[h] = maxcurr
            maxcurr = max(maxcurr, height[h])
    
        res = 0
        for h in range(len(height)):
            cap = min(maxleft[h], maxright[h]) - height[h]
            res += cap if cap > -1 else 0
            
        return res