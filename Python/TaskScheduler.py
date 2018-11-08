class Solution:
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        dic = {}
        for task in tasks:
            if task in dic:
                dic[task] += 1
            else:
                dic[task] = 1
                
        heap = []
        for task, count in dic.items():
            heapq.heappush(heap, -count)
        
        res = 0
        while heap:
            stack = []
            time = 0
            for _ in range(n+1):  #每个chunk有n+1个slots,每次取出count最大的任务
                if heap:
                    count = heapq.heappop(heap)
                    time += 1
                    if count < -1:
                        stack.append(count+1)
            for item in stack:
                heapq.heappush(heap, item)
            if heap:
                res += n+1
            else:
                res += time

        return res