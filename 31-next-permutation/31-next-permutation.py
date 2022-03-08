class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = len(nums) - 2
        while index >= 0 and nums[index] >= nums[index + 1]:
            index -= 1
        
        indexswap = len(nums) - 1
        while index >= 0 and indexswap >=0 and nums[indexswap] <= nums[index]:
            indexswap -= 1
        
        nums[index], nums[indexswap] = nums[indexswap], nums[index]
        nums[index + 1:] = sorted(nums[index + 1:])
        
        #sortit(index + 1, len(nums) - 1)
        
        return nums