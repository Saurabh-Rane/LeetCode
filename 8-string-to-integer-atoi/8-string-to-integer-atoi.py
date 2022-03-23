class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        isNegative = False
        result = 0
        
        if not s:
            return 0
        
        if s[0] == '-':
            isNegative = True
        elif s[0] == '+':
            isNegative = False
        elif not s[0].isnumeric():
            return 0
        else:
            result = ord(s[0]) - ord('0')
            
        for i in range(1, len(s)):
            if s[i].isnumeric():
                result = result * 10 + (ord(s[i]) - ord('0'))
                if isNegative and result > (2 ** 31):
                    return -(2 ** 31)
                elif not isNegative and result > (2 ** 31) - 1:
                    return (2 ** 31) - 1
            else:
                break
        
        if not isNegative:
            return result
        else:
            return -result