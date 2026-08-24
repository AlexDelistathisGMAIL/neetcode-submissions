class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)

        if length == 1:
            return 0

        minPrice = prices[0]
        maxProfit = 0

        for i in range(1, length):
            candidate = prices[i]
            if candidate > minPrice:
                currProfit = candidate - minPrice
                maxProfit = max(currProfit, maxProfit)
            minPrice = min(candidate, minPrice)

        return maxProfit
