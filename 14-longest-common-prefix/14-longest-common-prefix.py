class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ''
        
        for letter in range(len(strs[0])):
            for word in range(1, len(strs)):
                if letter == len(strs[word]) or strs[0][letter] != strs[word][letter]:
                    return res
            
            res += strs[0][letter]
        
        return res
        