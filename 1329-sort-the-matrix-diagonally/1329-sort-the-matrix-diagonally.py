class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        row = len(mat)
        col = len(mat[0])
        hashmap = collections.defaultdict(list)
        
        for i in range(row):
            for j in range(col):
                hashmap[i - j].append(mat[i][j])
                
        for i in hashmap:
            heapq.heapify(hashmap[i])
            
        for i in range(row):
            for j in range(col):
                mat[i][j] = heapq.heappop(hashmap[i - j])
                
        return mat
        