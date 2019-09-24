class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue=collections.deque()
        height={}
        queue.append((root,0))
        
        while queue:
            node,level=queue.popleft()
            if node:
                if level not in height:
                    height[level]=[node.val]
                else:
                    height[level].append(node.val)
            
            
                queue.append((node.left, level-1))
                queue.append((node.right, level+1))
        
        
        return [height[i] for i in sorted(height)]