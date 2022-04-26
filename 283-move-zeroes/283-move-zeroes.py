class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        for _ in range(len(nums)):
            if nums[count]==0:
                nums.pop(count)
                nums.append(0)
                continue
            count+=1