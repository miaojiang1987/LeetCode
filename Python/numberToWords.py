class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if not num:
            return 'Zero'

        self.less_20 = {1:'One',2:'Two',3:'Three',4:'Four',5:'Five',6:'Six',7:'Seven',8:'Eight',9:'Nine',
                            10:'Ten',11:'Eleven',12:'Twelve',13:'Thirteen',14:'Fourteen',15:'Fifteen',16:'Sixteen',
                            17:'Seventeen',18:'Eighteen',19:'Nineteen'}
        
        self.tenth = {2:'Twenty',3:'Thirty',4:'Forty',5:'Fifty',6:'Sixty',7:'Seventy',8:'Eighty',9:'Ninety'}
        
        self.thousands = ["","Thousand","Million","Billion"]
       
        res = ""
        for i in range(len(self.thousands)):
        # 三位为一个单位，如果超过3位数
            if num % 1000 != 0:
                res = self.get_three(num%1000) + " " + self.thousands[i] + " " + res
            num //= 1000

        return res.strip()        
    
    def get_two(self, num):
        if not num:
            return ''
        elif num<20:
            return self.less_20[num]
        else:
            ten=num//10
            rest=num-ten*10
            if rest:
                return self.tenth[ten]+ ' ' + self.less_20[rest] 
            else:
                return self.tenth[ten]
        
    def get_three(self, num):
        hundred= num//100
        rest=num-hundred*100
        if hundred and rest:
            return self.less_20[hundred]+' Hundred '+self.get_two(rest)
        elif hundred and not rest:
            return self.less_20[hundred]+ ' Hundred'            
        elif not hundred and rest:
            return self.get_two(rest)