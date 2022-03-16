class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter = []
        digit = []
        
        for log in logs:
            if log.split()[1].isdigit():
                digit.append(log)
            else:
                letter.append(log.split())
                
        letter.sort(key = lambda x : x[0])
        letter.sort(key = lambda x : x[1:])
        
        for log in range(len(letter)):
            letter[log] = " ".join(letter[log])
            
        letter.extend(digit)
        return letter
            
                
        
        