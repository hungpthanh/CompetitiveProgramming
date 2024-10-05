class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        min_value = prices[0]
        res = 0
        for price in prices:
            res = max(res, price - min_value)
            min_value = min(min_value, price)
        return res
