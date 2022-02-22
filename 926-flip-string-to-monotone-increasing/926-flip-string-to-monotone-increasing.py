class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        zero, one = 0, 0
        
        for x in range(s.index('1'), len(s)):
            if s[x] == '0':
                zero += 1
            else:
                one += 1
            if zero > one:
                zero = one
        
        return zero
        