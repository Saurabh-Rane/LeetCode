class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        res = []
        hashmap = collections.defaultdict(list)
        
        for i in range(len(groupSizes)):
            if len(hashmap[groupSizes[i]]) < groupSizes[i]:
                hashmap[groupSizes[i]].append(i)
            else:
                res.append(hashmap[groupSizes[i]])
                hashmap[groupSizes[i]] = [i]
            
        for i in hashmap:
            res.append(hashmap[i])
            
        return res
        