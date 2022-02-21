class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        for i in range(1, math.ceil(math.sqrt(n))):
            if not n % i:
                k -= 1
                if not k:
                    return i
                
        for i in range(int(math.sqrt(n)) , 0, -1):
            if not n % i:
                k -= 1
                if not k:
                    return int(n/i)
        
        return -1