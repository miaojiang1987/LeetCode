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
        
        pq=[]
        for item,count in hashmap.items():
            heapq.heappush(pq,-count)
        result=0
        
        while pq:
            stack=[]
            time=0
            for _ in range(n+1):
                if pq:
                    count=heapq.heappop(pq)
                    time+=1
                    if count<-1:
                        stack.append(count+1)
            
            for item in stack:
                heapq.heappush(pq,item)
            
            if pq:
                result+=n+1
            else:
                result+=time
        
        return result