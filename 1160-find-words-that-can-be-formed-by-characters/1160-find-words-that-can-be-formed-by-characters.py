class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        
        counter = collections.Counter(chars)
        res = 0
        
        for word in words:
            flag = True
            temp = collections.Counter(word)
            for l in word:
                if not (l in counter and counter[l] >= temp[l]):
                    flag = False
                if not flag:
                    break
            if flag:
                res += len(word)
                
        return res
                    