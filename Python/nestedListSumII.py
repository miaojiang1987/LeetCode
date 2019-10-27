class Solution(object):
    def depthSumInverse(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        if not nestedList:
            return 0
        queue=collections.deque()
        result=0
        maxDepth=1
        dic = collections.defaultdict(list)
        
        for item in nestedList:
            queue.append((item,1))
            while queue:
                cur,depth=queue.popleft()
                maxDepth=max(depth,maxDepth)
                if cur.isInteger():
                    dic[depth].append(cur.getInteger())
                else:
                    for element in cur.getList():
                        queue.append((element,depth+1))
        
        for level in dic:
            for num in dic[level]:
                result+=num*(maxDepth-level+1)
        
        return result