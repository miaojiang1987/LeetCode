class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None
        
        queue=collections.deque([node])
        
        hashmap={}
        hashmap[node]=Node(node.val,[])
        
        while queue:
            element=queue.popleft()
            for neighbor in element.neighbors:
                if neighbor not in hashmap:
                    hashmap[neighbor]=Node(neighbor.val,[])
                    queue.append(neighbor)
                hashmap[element].neighbors.append(hashmap[neighbor])
        
        return hashmap[node]