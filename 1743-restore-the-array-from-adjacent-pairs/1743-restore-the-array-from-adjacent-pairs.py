class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        hashmap = collections.defaultdict(list)
        res = []
        seen = set()
        
        for i, j in adjacentPairs:
            hashmap[i].append(j)
            hashmap[j].append(i)
            
        curr = None
        for i in hashmap:
            if len(hashmap[i]) == 1:
                curr = i
                break
        
        while curr != None:
            res.append(curr)
            seen.add(curr)
            adj = hashmap[curr]
            curr = None
            
            for i in adj:
                if i not in seen:
                    curr = i
                    break
        return res