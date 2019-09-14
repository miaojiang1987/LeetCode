from collections import defaultdict
class Solution(object):
    def verticalTraversal(self, root):
        self.res = collections.defaultdict(list)
        
        def dfs(root, layer, col):
            if root:
                self.res[col].append((col, layer, root.val))
                dfs(root.left, layer + 1, col - 1)
                dfs(root.right, layer + 1, col + 1)
        
        dfs(root, 0, 0)
        values = [sorted(self.res[key]) for key in sorted(self.res)]
        return [[val for _, _, val in col_val] for col_val in values]