class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        freq = collections.defaultdict(int)
        res = []
        
        for text in cpdomains:
            count, domain = text.split()
            subdomains = domain.split('.')
            for subdomain in range(len(subdomains)):
                freq['.'.join(subdomains[subdomain:])] += int(count)
                
        for i in freq:
            res.append(str(freq[i]) + ' ' + i )
            
        return res
            
        