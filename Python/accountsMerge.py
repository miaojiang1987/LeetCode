class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        em_to_name={}
        graph=collections.defaultdict(set)
        
        for account in accounts:
            name=account[0]
            for email in account[1:]:
                em_to_name[email]=name
                graph[account[1]].add(email)
                graph[email].add(account[1])
        
        visited=set()
        result=[]
        
        for email in graph:
            if email not in visited:
                stack=[email]
                visited.add(email)
                temp=[]
                while stack:
                    node=stack.pop()
                    temp.append(node)
                    for neigh in graph[node]:
                        if neigh not in visited:
                            stack.append(neigh)
                            visited.add(neigh)
        
                result.append([em_to_name[email]]+sorted(temp))
            
        
        return result