class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        hashmap={}
        for c in tasks:
            if c not in hashmap:
                hashmap[c]=1
            else:
                hashmap[c]+=1
        heap=[]
        for task,count in hashmap.items():
            heapq.heappush(heap,-count)
        
        result=0
        
        while heap:
            stack=[]
            time=0
            for _ in range(n+1):
                if heap:
                    count=heapq.heappop(heap)
                    time+=1
                    if count<-1:
                        stack.append(count+1)
            for item in stack:
                heapq.heappush(heap,item)
            
            if heap:
                result+=n+1
            else:
                result+=time
        
        return result