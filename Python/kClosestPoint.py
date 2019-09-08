class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        result=points
        self.sort(result,0,len(result)-1,K)
        return result[:K]
    
    def sort (self, points, l, r, K):
        # Partially sorts A[i:j+1] so the first K elements are
        # the smallest K elements.
        if l >= r:
            return 

        p = self.partition(points, l, r)
        if p > K: # 左侧没完全sort好 
            self.sort(points, l, p-1, K)
        else:
            self.sort(points, p+1, r, K)
    
    def partition(self,points,l,r):
        p = l
        pivot = self.distance(points[p])
        l += 1
 
        while l <= r:
            while l <= r and self.distance(points[l]) <= pivot:
                l += 1
            while l <= r and self.distance(points[r]) >= pivot:
                r -= 1
            if l < r:
                points[l], points[r] = points[r], points[l]
                
        points[p], points[r] = points[r], points[p]
        return r
    
    
    
    
    def distance(self,point):
        return point[0]**2+point[1]**2