class Solution(object):
    def depthSum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        result=0
        if not nestedList:
            return 0
        
        queue=[]
        for nested in nestedList:
            queue.append((nested,1))
        
        while queue: 
            for i in range(len(queue)):
                node,depth=queue.pop(0)
                if node.isInteger():
                    result+=depth*node.getInteger()
                else:
                    for lst in node.getList():
                        queue.append((lst,depth+1))
        
        
        return result
                