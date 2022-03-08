class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        count = 0
        queue = collections.deque()
        
        for i in s:
            while queue and queue[-1] == i and queue[0] != i:
                queue.pop()
            if queue and queue[-1] != i:
                queue.pop()
                count += 1
            queue.appendleft(i)
            
        return count