class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return None
        result=[]
        height=collections.defaultdict(list)
        
        queue=collections.deque()
        queue.append((root,0))
        
        while queue:
            node,level=queue.popleft()        
            if level in height:
                height[level].append(node.val)
            else:
                height[level]=[node.val]
            if node.left:
                queue.append((node.left,level-1))
            if node.right:
                queue.append((node.right,level+1))
        
        
        return [height[i] for i in sorted(height)]