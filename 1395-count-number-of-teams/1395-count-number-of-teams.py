class Solution:
    def numTeams(self, rating: List[int]) -> int:
        count = 0
        
        for i in range(len(rating)):
            leftmax, leftmin, rightmax, rightmin = 0, 0, 0, 0
            
            for j in range(i - 1 , -1, -1):
                if rating[j] < rating[i]:
                    leftmin += 1
                elif rating[j] > rating[i]:
                    leftmax += 1
                    
            for k in range(i + 1, len(rating), 1):
                if rating[k] < rating[i]:
                    rightmin += 1
                elif rating[k] > rating[i]:
                    rightmax += 1
            
            count += (leftmin * rightmax) + (leftmax * rightmin)
        
        return count