class Solution:
    def minSwaps(self, data: List[int]) -> int:
        
        totalOnes = data.count(1)
        
        currentOnes, maxOnes = 0, 0
        
        for i in range(len(data)):
            currentOnes += data[i]
            if i >= totalOnes:
                currentOnes -= data[i - totalOnes]
            maxOnes = max(maxOnes, currentOnes)
            
        return totalOnes - maxOnes
        