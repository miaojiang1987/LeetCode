class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        if not cpdomains:
            return []
        domain_stat={}
        results=[]
        for domain in cpdomains:
            cnt,url=domain.split(' ')
            domain_parts=url.split('.')
            name=''
            for i in range(len(domain_parts)-1,-1,-1):
                if name:
                    name=domain_parts[i]+'.'+name
                else:
                    name=domain_parts[i]
                if name not in domain_stat:
                    domain_stat[name]=int(cnt)
                else:
                    domain_stat[name]+=int(cnt)
                
        for key in domain_stat:
            results.append(str(domain_stat[key])+' '+key)
        
        
        return results