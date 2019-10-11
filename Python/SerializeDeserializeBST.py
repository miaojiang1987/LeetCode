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
        self.preorder(root,result)
        return ' '.join(result)
    
    def preorder(self,root,result):
        if root:
            result.append(str(root.val))
            self.preorder(root.left,result)
            self.preorder(root.right,result)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        queue=collections.deque(int(num) for num in data.split())
        return self.build(queue,float('-inf'),float('inf'))
        
    def build(self,queue,minval,maxval):
        if queue and minval<queue[0]<maxval:
            val=queue.popleft()
            node=TreeNode(val)
            node.left=self.build(queue,minval,val)
            node.right=self.build(queue,val,maxval)
            return node
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))