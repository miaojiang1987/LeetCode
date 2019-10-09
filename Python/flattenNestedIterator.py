# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.queue = []
        for item in nestedList:
            self.queue.append(item)
        

    def next(self):
        """
        :rtype: int
        """
        cur = self.queue.pop(0)
        return cur
        
        

    def hasNext(self):
        """
        :rtype: bool
        """
        while self.queue:
            cur = self.queue[0]
            if cur.isInteger():
                return True
            self.queue.pop(0)
            items = cur.getList()
            for i in range(len(items)):
                self.queue.insert(i, items[i])
        return False
        