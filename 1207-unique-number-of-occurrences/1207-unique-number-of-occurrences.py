class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hashmap = {}
        
        for i in arr:
            hashmap[i] = 1 + hashmap.get(i, 0)
            
        hashset = set()
        
        for i in hashmap:
            if hashmap[i] in hashset:
                return False
            hashset.add(hashmap[i])
            
        return True