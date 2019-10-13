"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        if not root:
            return ""
        
        queue = deque([root])
        bfs_order = []
        while queue:
            node = queue.popleft()
            bfs_order.append(str(node.val) if node else "#")
            if node:
                bfs_order[-1] = bfs_order[-1] + "/" + str(len(node.children))
                for child in node.children:
                    queue.append(child)
        
        return " ".join(bfs_order)
            
        
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        if not data:
            return None
        
        bfs_order = []
        for val in data.split():
            if '/' in val:
                parts = val.split('/')
                value, children_size = int(parts[0]), int(parts[1])
                node = Node(value, [None for _ in range(children_size)])
            else:
                node = Node(value, [])
            bfs_order.append(node)
            
        root = bfs_order[0]
        slow_index = 0
        
        nodes = [root]
        fast_index = 1
        
        while slow_index < len(nodes):
            node = nodes[slow_index]
            slow_index += 1
            
            for i in range(len(node.children)):
                node.children[i] = bfs_order[fast_index]
                fast_index += 1
                
            for i in range(len(node.children)):
                if node.children[i]:
                    nodes.append(node.children[i])
                    
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))