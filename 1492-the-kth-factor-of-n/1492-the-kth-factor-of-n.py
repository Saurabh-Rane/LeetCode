class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors = []
        for i in range(1, n + 1):
            factors.append(i) if n % i == 0 else None
            
        return factors[k - 1] if k <= len(factors) else -1