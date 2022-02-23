class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        maxSum = 0
        nums.sort()
        l, r = 0, len(nums) - 1
        while l < r:
            currSum = nums[l] + nums[r]
            maxSum = max(maxSum, currSum)
            l += 1
            r -= 1
        
        return maxSum