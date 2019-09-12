class Solution:
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        odd = ["0", "1", "8"]
        even = [""]
        if n % 2 == 1:
            res = odd
        else:
            res = even
            
        for i in range(n % 2, n - 1, 2):
            temp = []
            for s in res:
                if i != n-2:
                    temp.append("0"+s+"0")
                temp.append("1"+s+"1")
                temp.append("6"+s+"9")
                temp.append("8"+s+"8")
                temp.append("9"+s+"6")                
            res = temp

        return res