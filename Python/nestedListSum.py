class Solution(object):
    def depthSum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        if not nestedList:
            return 0
        total=0
        queue=[]
        
        for item in nestedList:
            queue.append((item,1))
        
        while queue:
            item,depth=queue.pop(0)
            if item.isInteger():
                total+=depth*item.getInteger()
            else:
                for new_Item in item.getList():
                    queue.append((new_Item,depth+1))
        
        
        return total