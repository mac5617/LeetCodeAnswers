class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}
        for index, value in enumerate(nums):
            attempt = target - nums[index]
            if attempt in lookup:
                return [index,lookup[attempt]]
            lookup[nums[index]] = index
            