class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        
        freqs = (collections.Counter(nums)).items()
        freqs = sorted(freqs, key = lambda x : [x[1], -x[0]])
        res = []
        
        for num, freq in freqs:
            res.extend([num for i in range(freq)])
        
        return res