class Solution(object):
    def rearrangeString(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        hashmap={}
        for c in s:
            if c not in hashmap:
                hashmap[c]=1
            else:
                hashmap[c]+=1
        
        queue=collections.deque()
        heap=[]
        
        for c,count in hashmap.items():
            heapq.heappush(heap, (-count, c))
        
        result=""
        
        while heap:
            count,c=heapq.heappop(heap)
            result+=c
            
            queue.append((count+1,c))
            
            if len(queue) >= k:
                count, c = queue.popleft()
                if count < 0:
                    heapq.heappush(heap, (count, c))
            
        
        if len(result) == len(s):
            return result
        
        return ""