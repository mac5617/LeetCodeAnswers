class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)
        for i in range(len(nums)):
            if nums[l] == min(nums[l:]):
                l+=1
            else:
                break
        for i in range(len(nums)):
            if nums[r-1] == max(nums[:r]):
                r-=1
            else:
                break
        return len(nums[l:r])
    
    