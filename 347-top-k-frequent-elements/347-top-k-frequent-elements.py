class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = collections.defaultdict(int)
        freq = [[] for i in range(len(nums) + 1)]
        res = []
        
        for val in nums:
            hashmap[val] += 1
        
        for val in hashmap:
            freq[hashmap[val]].append(val)
            
        for vals in range(len(freq) - 1, -1, -1):
            for val in freq[vals]:
                res.append(val)
                k -= 1
                if not k:
                    return res