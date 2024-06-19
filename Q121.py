class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Keep track of the price range from 0 and compare. 
        If at any point, is the price less than the buy, then change the value of buy. Or else change max_profit to the max of both values.
        """
        max_profit = 0
        buy = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            else:
                max_profit = max(max_profit, prices[i] - buy)
        return max_profit
