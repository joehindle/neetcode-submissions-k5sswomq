class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res=0
        for x in range(len(prices)):
            buy = prices[x]
            for y in range (x+1, len(prices)):
                sell = prices[y]
                res=max(res, sell-buy)
        return res
        