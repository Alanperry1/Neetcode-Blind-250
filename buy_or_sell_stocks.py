class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Time Complexity: O(n) - single pass through prices array
        # Space Complexity: O(1) - only using constant extra space
        l,r=0,1
        maxProfit=0
        while r<len(prices):
            if prices[l]<prices[r]:
                profit=prices[r]-prices[l]
                if profit>maxProfit:
                    maxProfit=profit
            else:
                l=r
            r+=1
        
        return maxProfit
