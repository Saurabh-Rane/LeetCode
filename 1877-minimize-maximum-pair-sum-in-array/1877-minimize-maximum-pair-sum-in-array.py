class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        maxp = 0
        
        left, right = 0, len(nums) - 1
        
        while left < right:
            maxp = max(maxp, nums[left] + nums[right])
            left += 1
            right -= 1
            
        return maxp
        