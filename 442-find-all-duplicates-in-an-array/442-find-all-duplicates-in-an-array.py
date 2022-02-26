class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        hashmap = collections.defaultdict(int)
        
        for i in nums:
            hashmap[i] += 1
            
        return [i for i in hashmap if hashmap[i] == 2]
        