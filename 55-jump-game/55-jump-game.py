class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cache = [0] * len(nums)
        cache[-1] = 1
        
        for i in range(len(nums) - 2, -1, -1):
            #print(cache[i:i+nums[i]+1])
            if 1 in cache[i : i + nums[i] + 1]:
                cache[i] = 1
            else:
                cache[i] = 0
        #print(cache)
        return True if cache[0] else False 