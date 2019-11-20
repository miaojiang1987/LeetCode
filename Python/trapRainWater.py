class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        result=0
        
        left_max=[0 for i in range(len(height))]
        maximum=0
        for i in range(len(height)):
            left_max[i]=maximum
            if height[i]>maximum:
                maximum=height[i]
        
        right_maximum=height[len(height)-1]
        
        for i in range(len(height)-2,-1,-1):
            max_height=min(right_maximum,left_max[i])
            if max_height>height[i]:
                result+=max_height-height[i]
            
            if height[i]>right_maximum:
                right_maximum=height[i]
        
        
        return result