class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        candynum = [1 for i in range(len(ratings))]
        for i in range(1,len(ratings)):
            if ratings[i]>ratings[i-1]:
                candynum[i] = candynum[i-1] + 1
        for i in range(len(ratings)-2, -1, -1):
            if ratings[i+1] < ratings[i] and candynum[i+1] >= candynum[i]:
                candynum[i] = candynum[i+1] + 1
        return sum(candynum)