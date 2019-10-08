class Solution:
    def maximumSwap(self, num: int) -> int:
        num = [c for c in str(num)]
        rightMax = num.copy()
        for i in range(len(num)-2, -1, -1):
            if rightMax[i] < rightMax[i+1]:
                rightMax[i] = rightMax[i+1]
        for i in range(len(rightMax)):
            if num[i]<rightMax[i]:
                for j in range(len(num)-1,i,-1):
                    if rightMax[i]==num[j]:
                        num[i], num[j] = num[j], num[i]
                        return "".join(num)
        
        
        return "".join(num)