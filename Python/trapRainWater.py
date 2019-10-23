class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        
        result=0
        
        left_dp=[0 for i in range(len(height))]
        left_max=height[0]
        left_dp[0]=0
        for i in range(1,len(height)):
            left_dp[i]=left_max
            left_max=max(left_max,height[i])
        
        right_max=height[len(height)-1]
        for i in range(len(height)-2,-1,-1):
            maximum=min(right_max,left_dp[i])
            if maximum>height[i]:
                result+=maximum-height[i]
            
            right_max=max(right_max,height[i])
        
        
        
        return result
                