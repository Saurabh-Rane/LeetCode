class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        length = len(colors)
        maxdistance = 0
        
        for i in range(1, length):
            if colors[i] != colors[0]:
                maxdistance = max(maxdistance, i)
        
        for j in range(length - 2, -1, -1):
            if colors[j] != colors[length - 1]:
                maxdistance = max(maxdistance, length - j - 1)
                
        return maxdistance