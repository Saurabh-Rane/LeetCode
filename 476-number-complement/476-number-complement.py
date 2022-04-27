class Solution:
    def findComplement(self, num: int) -> int:
        
        exor = 0
        temp = num
        
        while temp:
            exor = exor << 1
            exor ^= 1
            temp >>= 1
        
        return exor ^ num