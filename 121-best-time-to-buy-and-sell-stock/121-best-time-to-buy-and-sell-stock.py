class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        smallest = float('inf')
        largest = 0
        
        for i in prices:
            largest = max(i-smallest,largest)
            smallest = min(smallest,i)
        return largest