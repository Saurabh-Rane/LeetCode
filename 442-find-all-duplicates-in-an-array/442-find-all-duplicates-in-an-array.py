class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        output = []
        
        for i in nums:
            val = abs(i)
            if nums[val - 1] < 0:
                output.append(val)
            else:
                nums[val - 1] *= -1
                
        return output