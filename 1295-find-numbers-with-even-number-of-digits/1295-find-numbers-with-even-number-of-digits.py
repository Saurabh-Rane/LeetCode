class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        res = 0
        for i in nums:
            res = res + 1 if len(str(i)) % 2 == 0 else res
        return res