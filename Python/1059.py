class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        g = {}
        for a,b in edges:
            g.setdefault(a,[]).append(b)
        if destination in g:
            return False

        def dfs(root,path):            
            if root not in g:
                return root == destination                

            path.add(root)
            for n in g[root]:
                if n in path or not dfs(n,path):
                    return False
            path.remove(root)   
            return True


        return dfs(source,set())
