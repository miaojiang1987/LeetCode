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
        if not root:
            return result
        queue=collections.deque()
        queue.append(root)
        while queue:
            node=queue.popleft()
            if node:
                result.append(node.val)
            else:
                result.append('null')
            if node:
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
        queue=collections.deque()
        root=TreeNode(int(data[0]))
        queue.append(root)
        i=1
        while queue and i<len(data):
            node=queue.popleft()
            if data[i]!='null':
                node.left=TreeNode(int(data[i]))
                queue.append(node.left)
            i+=1
            if data[i]!='null':
                node.right=TreeNode(int(data[i]))
                queue.append(node.right)
            i+=1
        
        return root