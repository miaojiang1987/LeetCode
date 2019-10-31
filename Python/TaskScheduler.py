class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        hashmap={}
        for task in tasks:
            if task in hashmap:
                hashmap[task]+=1
            else:
                hashmap[task]=1
            
        result=0
        pq=[]
        for key in hashmap:
            count=hashmap[key]
            heapq.heappush(pq,-count)
        
        for i in range(len(tasks)):
            stack=[]
            item=0
            for _ in range(n+1):
                if pq:
                    count=heapq.heappop(pq)
                    item+=1
                    if count<-1:
                        stack.append(count+1)
            
            for item in stack:
                heapq.heappush(pq,item)
            
            if pq:
                result+=n+1
            else:
                result+=item
        
        
        
        return result