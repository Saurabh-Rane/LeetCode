class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        
        maxdistance = 0
        
        for i in range(1, len(colors)):
            if colors[i] != colors[0]:
                maxdistance = max(maxdistance, i)
        
        for j in range(len(colors) - 2, -1, -1):
            if colors[j] != colors[len(colors) - 1]:
                maxdistance = max(maxdistance, len(colors) - j - 1)
                
        return maxdistance