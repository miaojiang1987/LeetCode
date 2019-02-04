class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        temp=[]
        result=[]

        self.helper(root,sum,result,temp)
        
        return result
    
    def helper(self,root,sum,result,tmp):
        if not root: return 
        remain=sum-root.val
        
        if not root.left and not root.right:
            if remain==0:
                result.append(tmp+[root.val])
        
        else:
            self.helper(root.left,remain,result,tmp+[root.val])
            self.helper(root.right,remain,result,tmp+[root.val])