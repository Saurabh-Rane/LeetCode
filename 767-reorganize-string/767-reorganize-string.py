class Solution:
    def reorganizeString(self, s: str) -> str:
        hashmap = Counter(s)
        
        heap = [[-count, letter] for letter, count in hashmap.items()]
        heapq.heapify(heap)
        prev = None
        res = ''
        
        while heap or prev:
            if prev and not heap:
                return ''
            
            count, letter = heapq.heappop(heap)
            res += letter
            count += 1
            
            if prev:
                heapq.heappush(heap, prev)
                prev = None
            
            if count:
                prev = [count, letter]
                
        return res
        
        