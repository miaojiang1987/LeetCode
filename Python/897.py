class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def inorder(node):
            if node:
                inorder(node.left)
                node.left=None
                self.cur.right=node
                self.cur=node
                inorder(node.right)
        
        ans=self.cur=TreeNode(None)
        inorder(root)
        
        return ans.right