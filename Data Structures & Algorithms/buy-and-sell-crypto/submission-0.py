class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyPrice = prices[0]
        profit = 0
        oldProfit = 0
        
        for i in prices[1::]:
            if i < buyPrice:
                buyPrice = i

                if profit > oldProfit:
                     oldProfit = profit

            elif i > buyPrice:
                profit = max(i - buyPrice, profit)

        return max(profit, oldProfit)