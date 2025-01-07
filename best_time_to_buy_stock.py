class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0,1
        bestProfit = 0

        while(r <= len(prices) - 1):
            if(prices[l] < prices[r]):
                profit = prices[r] - prices[l]
                if profit > bestProfit:
                    bestProfit = profit
            else:
                l = r
            r += 1
        return bestProfit