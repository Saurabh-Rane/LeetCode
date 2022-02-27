class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        if len(nums) == 1:
            return [nums[:]]
        
        for i in range(len(nums)):
            val = nums.pop(0)
            pers = self.permute(nums)
            for per in pers:
                per.append(val)
            res.extend(pers)
            nums.append(val)
            
        return res