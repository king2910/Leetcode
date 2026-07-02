class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min: int =prices[0]
        max: int =0
        for i in range(1,len(prices)):
            if prices[i]<min:
                min=prices[i]
            if (prices[i]-min)>max:
                max=prices[i]-min
        return max