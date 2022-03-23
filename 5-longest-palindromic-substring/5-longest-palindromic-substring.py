class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        resLen = 0
        
        for i in range(len(s)):
            # odd length substring
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                currLen = r - l + 1
                if currLen > resLen:
                    resLen = currLen
                    res = s[l:r + 1]
                l -= 1
                r += 1
                
            # even length substring
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                currLen = r - l + 1
                if currLen > resLen:
                    resLen = currLen
                    res = s[l:r + 1]
                l -= 1
                r += 1
                
        return res