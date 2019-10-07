class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        leftStack = []
        starStack = []
        
        for idx, char in enumerate(s):
            if char == "(":
                leftStack.append((idx,char))
            elif char == "*":
                starStack.append((idx,char))
            else:
                if len(leftStack) != 0:
                    leftStack.pop()
                else:
                    if len(starStack) != 0:
                        starStack.pop()
                    else:
                        return False
        
        while len(leftStack) > 0 and len(starStack) > 0:
            if starStack[-1][0] < leftStack[-1][0]:
                return False
            else:
                starStack.pop()
                leftStack.pop()
        
        return len(starStack) >= len(leftStack) 