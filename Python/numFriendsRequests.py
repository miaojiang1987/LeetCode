class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        
        res, numInAge, sumInAge = 0, [0] *121, [0]*121 #长度121因为0到120
        # get a count for each age in array 
        for i in ages:
            numInAge[i] +=1 
        #print(numInAge)
        # calculate count of age + previous age sum 
        for i in range(1,121):
            sumInAge[i] = numInAge[i] + sumInAge[i-1]
        #print(sumInAge)
        #print(numInAge)
        for i in range(15, 121):
            if numInAge[i] == 0:
                continue
            count = sumInAge[i] - sumInAge[int(i/2) + 7]
            #print(count)
            res += count *numInAge[i] - numInAge[i] # remove self as count in friend
        return res