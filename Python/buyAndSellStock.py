class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        profit=0
        min_price=prices[0]
        
        for i in range(len(prices)):
            if min_price>prices[i]:
                min_price=prices[i]
            
            profit=max(profit,prices[i]-min_price)
        
        return profit