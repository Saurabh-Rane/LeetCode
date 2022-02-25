class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        queue = collections.deque()
        
        for i in range(1, n + 1):
            queue.appendleft(i)
        
        while len(queue) != 1:
            for i in range(1, k):
                queue.appendleft(queue[-1])
                queue.pop()
            queue.pop()
            
        return queue.pop()