class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hashmap = {}
        
        for i in arr:
            hashmap[i] = 1 + hashmap.get(i, 0)
            
        hashset = set()
        
        if len(hashmap.values()) != len(set(hashmap.values())):
            return False
        else:
            return True