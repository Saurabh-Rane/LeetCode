class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        count = []
        
        for i in nums:
            val = abs(i)
            if nums[val - 1] < 0:
                count.append(val)
            else:
                nums[val - 1] *= -1
            
        return count
        