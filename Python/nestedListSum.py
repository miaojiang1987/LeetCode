class Solution:
    def depthSum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        if not nestedList:
            return 0
        
        result=0
        queue=[]
        for item in nestedList:
            queue.append((item,1))
        
        while queue:
            item,level=queue.pop()
            if item.isInteger():
                result+=item.getInteger()*level
            else:
                for newItem in item.getList():
                    queue.append((newItem,level+1))
        
        return result