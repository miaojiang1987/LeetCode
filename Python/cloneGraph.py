"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None
        hashmap={}
        queue=collections.deque()
        queue.append(node)
        hashmap[node]=Node(node.val,[])
        
        while queue:
            temp=queue.popleft()
            for nei in temp.neighbors:
                if nei not in hashmap:
                    hashmap[nei]=Node(nei.val,[])
                    queue.append(nei)
                hashmap[temp].neighbors.append(hashmap[nei])
        
        
        return hashmap[node]