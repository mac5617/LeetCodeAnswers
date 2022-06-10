class Solution:
    def minSwaps(self, data: List[int]) -> int:
        # binary array so there are only ones and zeros. Find all ones in array.
        windowLength = sum(data)
        # Same concept to find create our sliding window
        windowOnes = sum(data[:windowLength])
        # return value which is used to compare the optimal window
        maxOnes = windowOnes
        # loop that goes through the window range
        for i in range(windowLength,len(data)):
            # add and remove ones according to the value
            windowOnes -= data[i-windowLength]
            windowOnes += data[i]
            maxOnes = max(windowOnes,maxOnes)
        return windowLength - maxOnes
        