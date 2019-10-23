class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        if not root:
            return -1
        dist=float('inf')
        result=0
        while root:
            if root.val==target:
                return root.val
            
            if dist>abs(root.val-target):
                dist=abs(root.val-target)
                result=root.val
            if target>root.val:
                root=root.right
            else:
                root=root.left
        
        return result