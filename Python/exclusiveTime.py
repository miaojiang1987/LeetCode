class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        stack=[]
        result=[0]*n
        prev_time=0
        
        for log in logs:
            idx, category, time = log.split(':')
            if category=='start':
                if stack:
                    result[stack[-1]]+=int(time)-prev_time
                stack.append(int(idx))
                prev_time=int(time)
            
            else:
                result[stack[-1]] += int(time) - prev_time + 1
                stack.pop()
                prev_time = int(time) + 1
        
        return result