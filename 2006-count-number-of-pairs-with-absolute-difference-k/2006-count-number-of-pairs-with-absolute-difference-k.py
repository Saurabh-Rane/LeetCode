class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        hashmap = collections.defaultdict(int)
        count = 0
        
        for i in nums:
            num1, num2 = i - k, i + k
            if num1 in hashmap:
                count += hashmap[num1]
            if num2 in hashmap:
                count += hashmap[num2]
            hashmap[i] += 1
            
        return count