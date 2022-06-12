class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        seen = {}
        left = 0
        runSum,output = 0,0
        for index,value in enumerate(nums):
            if value in seen:
                while left < seen[value]+1:
                    runSum-=nums[left]
                    left+=1
            seen[value] = index
            runSum+=value
            output = max(runSum,output)
        return output