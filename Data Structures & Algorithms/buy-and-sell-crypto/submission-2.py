class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        maxProfit = 0
        while right < len(prices):
            if  prices[right] > prices[left]:
                profit = prices[right] - prices[left] 
                maxProfit = max(profit,maxProfit)
                right+=1
            elif prices[right] < prices[left] :
                left=right
                right+=1
            else:
                right+=1
        return maxProfit
        