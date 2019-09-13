res = 0
    def strobogrammaticInRange(self, low, high):
        """
        :type low: str
        :type high: str
        :rtype: int
        """
        for length in range(len(low),len(high)+1):
            self.dfsHelper(low,high, length, "")
            self.dfsHelper(low,high, length, "1")
            self.dfsHelper(low,high, length, "8")
            self.dfsHelper(low,high, length, "0")
        return self.res
            
        
        
    def dfsHelper(self,low,high,length,path):
        if len(path) > length:
            return
        if len(path) == length:
            if len(path) != 1 and path[0] == '0':
                return
            else:
                if int(path) >= int(low) and int(path) <= int(high):
                    self.res +=1
                return
        self.dfsHelper(low,high, length, '0'+path+'0')
        self.dfsHelper(low,high, length, '6'+path+'9')
        self.dfsHelper(low,high, length, '9'+path+'6')
        self.dfsHelper(low,high, length, '8'+path+'8')
        self.dfsHelper(low,high, length, '1'+path+'1')