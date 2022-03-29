class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right, maxP = 0, 1, 0
        
        while right < len(prices):
            if prices[left] < prices[right]:
                currP = prices[right] - prices[left]
                maxP = max(maxP, currP)
            else:
                left = right
            right += 1
            
        return maxP