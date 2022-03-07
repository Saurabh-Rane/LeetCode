class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        maxL = 0
        hashset = set()
        l, r = 0, 0
        
        while r < len(s):
            if s[r] not in hashset:
                hashset.add(s[r])
                maxL = max(maxL, r - l + 1)
                r += 1
            else:
                hashset.remove(s[l])
                l += 1
                
        return maxL
                
            
        