class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        res = [0] * k
        hashmap = collections.defaultdict(set)
        
        for i,j in logs:
            hashmap[i].add(j)
            
        for i in hashmap:
            res[len(hashmap[i]) - 1] += 1
            
        return res
            