class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        hashmap={}
        for task in tasks:
            if task not in hashmap:
                hashmap[task]=1
            else:
                hashmap[task]+=1
        
        pq=[]
        for task in hashmap:
            count=hashmap[task]
            heapq.heappush(pq,-count)
        result=0
        
        while pq:
            stack=[]
            item=0
            for _ in range(n+1):
                
                if pq:
                    count=heapq.heappop(pq)
                    item+=1
                    if count<-1:
                        stack.append(count+1)
                        
            
            for element in stack:
                heapq.heappush(pq,element)
            
            
            if pq:
                result+=n+1
            else:
                result+=item
        
        return result