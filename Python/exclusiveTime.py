class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        if not logs:
            return None
        result=[0]*n
        stack=[]
        prev_time=0
        
        for log in logs:
            ID,category,time=log.split(':')
            if category=='start':
                if stack:
                    result[stack[-1]]+=int(time)-prev_time
                stack.append(int(ID))
                prev_time=int(time)
            else:
                result[stack[-1]]+=int(time)-prev_time+1
                stack.pop()
                prev_time=int(time)+1
        
        
        return result