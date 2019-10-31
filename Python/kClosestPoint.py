class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        l=0
        r=len(points)-1
        while l<=r:
            p=self.partition(points,l,r)
            if p==K:
                return points[:K]
            
            elif p>K:
                r=p-1
            
            else:
                l=p+1
        return points[:K]
    
    def partition(self,points,l,r):
        p=l
        pivot=self.distance(points[p])
        
        while l<=r:
            while l<=r and self.distance(points[l])<=pivot:
                l+=1
            
            while l<=r and self.distance(points[r])>=pivot:
                r-=1
            
            if l<r:
                points[l],points[r]=points[r],points[l]
                l+=1
                r-=1
        
        points[p],points[r]=points[r],points[p]
        return r
        
    
    
    
    def distance(self,p):
        return p[0]**2+p[1]**2