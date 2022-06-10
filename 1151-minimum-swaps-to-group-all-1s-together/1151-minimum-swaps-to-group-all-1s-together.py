class Solution:
    def minSwaps(self, data: List[int]) -> int:
        windowLength = sum(data)
        windowOnes = sum(data[:windowLength])
        maxOnes = windowOnes
        for i in range(windowLength,len(data)):
            windowOnes -= data[i-windowLength]
            windowOnes += data[i]
            maxOnes = max(windowOnes,maxOnes)
        return windowLength - maxOnes
        