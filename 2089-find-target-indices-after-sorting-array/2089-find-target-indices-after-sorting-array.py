class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        ans = []
        nums.sort()
        
        for i in range(len(nums)):
            if nums[i] == target:
                ans.append(i)
            # break when all target elements are checked     
            elif ans:
                break
                
        return ans
        
        
        