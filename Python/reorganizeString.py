class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        hashmap={}
        for s in S:
            if s not in hashmap:
                hashmap[s]=1
            else:
                hashmap[s]+=1
        
        result=''
        heap=[]
        
        for key,count in hashmap.items():
            heapq.heappush(heap,[-count,key])
        
        while heap:
            if len(heap)>=2:
                item1=heapq.heappop(heap)
                item2=heapq.heappop(heap)
                
                result+=item1[1]
                result+=item2[1]
                
                item1[0]+=1
                item2[0]+=1
                
                if item1[0]<0:
                    heapq.heappush(heap,item1)
                
                if item2[0]<0:
                    heapq.heappush(heap,item2)
            
            else:
                item=heapq.heappop(heap)
                if item[0]<-1:
                    return ''
                result+=item[1]
         
        return result