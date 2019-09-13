class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        result=[]
        path=''
        if not root: return result       
        self.helper(root,result,path)
        return result
    
    def helper(self,node,result,path):
        if node:
            path+=str(node.val)
            if not node.left and not node.right:
                result.append(path)
            
            else:
                self.helper(node.left,result,path+"->")
                self.helper(node.right,result,path+"->")