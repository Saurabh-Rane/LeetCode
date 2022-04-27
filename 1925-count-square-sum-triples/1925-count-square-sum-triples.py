class Solution:
    def countTriples(self, n: int) -> int:
        
        count = 0
        
        for i in range(1, n):
            for j in range(i + 1, n):
                square = i * i + j * j
                sqroot = math.sqrt(square)
                if int(sqroot) == sqroot and sqroot <= n:
                    count += 2
            
        return count