class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack=[]
        self.minstack=[]

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        if not self.minstack or x<=self.minstack[-1]:
            self.minstack.append(x)

    def pop(self):
        """
        :rtype: None
        """
        if self.stack:
            x=self.stack[-1]
            self.stack=self.stack[:-1]
            if x==self.minstack[-1]:
                self.minstack=self.minstack[:-1]
        return x
        

    def top(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if self.minstack:
            return self.minstack[-1]
