class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit=0
        
        if not prices or len(prices)==0:
            return 0
        
        min_price=prices[0]
        
        for i in range(len(prices)):
            if prices[i]<min_price:
                min_price=prices[i]
            else:
                profit=max(profit,prices[i]-min_price)
        
        return profit