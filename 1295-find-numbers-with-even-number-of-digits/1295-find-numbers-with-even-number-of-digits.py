class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        res = 0
        for i in nums:
            count = 0
            while i:
                count += 1
                i //= 10
            res = res + 1 if (count % 2) == 0 else res
        return res