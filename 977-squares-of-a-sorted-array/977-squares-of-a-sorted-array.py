class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        i, j = 0, len(nums)- 1
        pointer = j
        while i <= j:
            if abs(nums[i]) < abs(nums[j]):
                res[pointer] = nums[j] * nums[j]
                j -= 1
            else:   
                res[pointer] = nums[i] * nums[i]
                i +=1
            pointer -= 1
            
        return res