class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        a, b = 0, 0
        n, m = len(firstList), len(secondList)
        res = []
        
        while a < n and b < m: 
            start = max(firstList[a][0], secondList[b][0])
            end = min(firstList[a][1], secondList[b][1])
            
            if start <= end:
                res.append([start, end])
                
            if firstList[a][1] < secondList[b][1]:
                a += 1
            else:
                b += 1
                
        return res