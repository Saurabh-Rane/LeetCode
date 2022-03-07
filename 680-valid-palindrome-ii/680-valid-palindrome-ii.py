class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        
        def palindromecheck(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                else:
                    l += 1
                    r -= 1
            return True
        
        while l < r:
            if s[l] != s[r]:
                return palindromecheck(l + 1, r) or palindromecheck(l, r - 1)
            else:
                l += 1
                r -= 1
        return True
    
        
        