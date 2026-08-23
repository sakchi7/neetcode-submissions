class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        if len(prices) <= 1:
            return profit
        i = 0
        j = 1
        while j < len(prices):
            if prices[i] < prices[j]:
                curr = prices[j] - prices[i]
                profit = max(profit, curr)
            else:
                i = j
            j += 1
        return profit
        
        