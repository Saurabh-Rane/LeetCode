class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        #previous security device count
        psdc = 0
        res = 0
        for i in bank:
            count = 0
            for device in i:
                if device == '1':
                    count += 1
            res += count * psdc
            if count:
                psdc = count
        
        return res
                
        