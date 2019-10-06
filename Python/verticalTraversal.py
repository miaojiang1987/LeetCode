class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        seen = collections.defaultdict(
                  lambda: collections.defaultdict(list))

        def dfs(node, x=0, y=0):
            if node:
                seen[x][y].append(node)
                dfs(node.left, x-1, y+1)
                dfs(node.right, x+1, y+1)

        dfs(root)
        ans = []

        for x in sorted(seen):
            report = []
            for y in sorted(seen[x]):
                report.extend(sorted(node.val for node in seen[x][y]))
            ans.append(report)

        return ans