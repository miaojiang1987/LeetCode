class Solution(object):
    def pathSum(self, root, sum):
        def traverse(root, val):
            if not root:
                return 0
            res = (val == root.val)
            res += traverse(root.left, val - root.val)
            res += traverse(root.right, val - root.val)
            return res
        if not root:
            return 0
        ans = traverse(root, sum)
        ans += self.pathSum(root.left, sum)
        ans += self.pathSum(root.right, sum)
        return ans