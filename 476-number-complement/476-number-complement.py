class Solution:
    def findComplement(self, num: int) -> int:
        res = 0
        
        i = 0
        while num:
            rem = 0 if num % 2 else 1
            res = (rem * (10 ** i)) + res
            num = num // 2
            i += 1
        #print(res)
        
        i = 0
        while res:
            rem = res % 10
            num += rem * (2 ** i)
            i += 1
            res = res // 10
            
        return num