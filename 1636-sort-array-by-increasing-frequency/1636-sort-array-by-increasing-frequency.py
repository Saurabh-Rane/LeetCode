class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        
        counter = collections.Counter(nums)
        nums.sort(key = lambda x : (counter[x], -x))
        
        return nums