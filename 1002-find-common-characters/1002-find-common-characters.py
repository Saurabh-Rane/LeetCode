class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        
        res = []
        alpha = [float("inf") for i in range(26)]
        
        for word in words:
            curralpha = [0 for i in range(26)]
            for letter in word:
                curralpha[ord(letter) - ord('a') ] += 1  
            for count in range(26):
                alpha[count] = min(alpha[count], curralpha[count])
                
        for i in range(26):
            while alpha[i] > 0:
                res.append(chr(ord('a') + i))
                alpha[i] -= 1
                
        return res