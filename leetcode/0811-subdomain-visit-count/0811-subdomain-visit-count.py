from collections import defaultdict

class Solution:
    def subdomainVisits(self, cpdomains: list[str]) -> list[str]:
        counts = defaultdict(int)
        
        for cpdomain in cpdomains:
            count, domain = cpdomain.split()
            count = int(count)
            fragments = domain.split(".")
            
            
            for i in range(len(fragments)):
                subdomain = ".".join(fragments[i:])
                counts[subdomain] += count
        
        
        return [f"{ct} {dom}" for dom, ct in counts.items()]