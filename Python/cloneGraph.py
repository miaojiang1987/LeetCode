class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None
        
        queue=[node]
        hashmap={}
        hashmap[node]=Node(node.val,[])
        
        while queue:
            element=queue.pop(0)
            for neighbor in element.neighbors:
                if neighbor not in hashmap:
                    queue.append(neighbor)
                    hashmap[neighbor]=Node(neighbor.val,[])                    
                hashmap[element].neighbors.append(hashmap[neighbor])
                
        return hashmap[node]