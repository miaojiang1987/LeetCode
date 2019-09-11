class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        right_most_value=dict()
        max_depth=-1
        queue=collections.deque([(root,0)])
        
        while queue:
            node,depth=queue.popleft()
            
            if node is not None:
                max_depth=max(max_depth,depth)
                
                right_most_value[depth]=node.val
                
                queue.append((node.left,depth+1))
                queue.append((node.right,depth+1))
        
        
        return [right_most_value[depth] for depth in range(max_depth+1)]
          