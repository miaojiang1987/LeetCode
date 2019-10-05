class Solution(object):
    def dailyTemperatures(self, T):
        if not T:
            return []
        result=[0 for i in range(len(T))]
        queue=collections.deque()
        
        for i in range(len(T)):
            #while queue and T[i]>T[queue[0]]:
            #    index=queue.popleft()
            #    result[index]=i-index
            while queue and T[i]>T[queue[-1]]:
                index=queue.pop()
                result[index]=i-index
            queue.append(i)
           
        return result