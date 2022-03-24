class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x : x[0])
        res = [intervals[0]]
        
        for i in range(1,len(intervals)):
            start, end = intervals[i]
            endPrev = res[-1][1]
            
            if start <= endPrev:
                res[-1][1] = max(endPrev, end)
            else:
                res.append([start, end])
                
        return res