class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        hashset = collections.defaultdict(set)
        ans = [0] * k
        
        for i, j in logs:
            hashset[i].add(j)
            
        for i in hashset:
            ans[len(hashset[i]) - 1] += 1
            
        return ans
        