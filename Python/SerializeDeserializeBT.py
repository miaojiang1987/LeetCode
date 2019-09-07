from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        result=[]
        queue=deque()
        queue.append(root)
        while queue:
            node=queue.popleft()
            if not node:
                result.append("null")
                continue
            else:
                result.append(node.val)
                
            queue.append(node.left)
            queue.append(node.right)
        
        return result

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data or data[0]=='null':
            return None
        queue=deque()
        root=TreeNode(data[0])
        queue.append(root)
        i=1
        while queue and i < len(data):
            node=queue.popleft()
            if data[i]!='null':
                node.left=TreeNode(data[i])
                queue.append(node.left)
            i+=1
            if data[i]!='null':
                node.right=TreeNode(data[i])
                queue.append(node.right)
            i+=1
        return root