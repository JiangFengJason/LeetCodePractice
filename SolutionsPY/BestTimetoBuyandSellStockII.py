class Best:
    def maxProfit(self, prices):
        maxPro=0
        for i in range(1,len(prices)):
            if prices[i]>prices[i-1]:
                maxPro+=prices[i]-prices[i-1]
        return maxPro