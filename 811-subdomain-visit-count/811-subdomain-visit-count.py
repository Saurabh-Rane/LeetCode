class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        res = collections.defaultdict(int)
        temp = []
        for i in cpdomains:
            count, text = i.split()
            count = int(count)
            subtext = text.split(".")
            for j in range(len(subtext)):
                res['.'.join(subtext[j:])] += count
                
        for i, j in res.items():
            temp.append(str(j) + ' ' + str(i))
        
        return temp
            