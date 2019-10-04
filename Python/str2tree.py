# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def str2tree(self, s):
        """
        :type s: str
        :rtype: TreeNode
        """
        if not s:
            return None
        stack=[]
        string=""
        
        for i in range(len(s)):
            if s[i]!='(' and s[i]!=')':
                string+=s[i]
        
            else:
                if string:
                    value=int(string)
                    stack.append(TreeNode(value))
                    string=""
                if s[i]==')':
                    node=stack.pop()
                    if stack[-1].left:
                        stack[-1].right=node
                    else:
                        stack[-1].left=node
        if string:
            stack.append(TreeNode(int(string)))
        return stack[-1]