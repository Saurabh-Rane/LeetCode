class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        return [i for i, j in collections.Counter(nums).items() if j > 1]