class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        ans = -1
        for i in range(1, n + 1):
            if n % i == 0:
                k -= 1
                ans = i if k == 0 else ans
        
        return ans
            
        