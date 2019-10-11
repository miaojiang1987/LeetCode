class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        self.helper(n, n, "", result)
        return result

    def helper(self, left, right, current, result):
        if left == 0 and right == 0:
            result.append(current)
            return
        if left > 0:
            self.helper(left - 1, right, current + "(", result)
        if right > left:
            self.helper(left, right - 1, current + ")", result)