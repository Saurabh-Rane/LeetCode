class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] % 2 == 0:
                left += 1
            if nums[right] % 2 == 1:
                right -= 1
            if nums[left] % 2 == 1 and nums[right] % 2 == 0 and left < right:
                temp = nums[right]
                nums[right] = nums[left]
                nums[left] = temp
            
        return nums