class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapq.heapify(sticks)
        res = 0
        
        while len(sticks) > 1:
            total = heapq.heappop(sticks) + heapq.heappop(sticks)
            res += total
            heapq.heappush(sticks, total)
            
        return res
        