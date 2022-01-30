class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        count = len(nums)
        nums = list(set(nums))
        nums.sort()
        pointer = 0
        for i in range(1,count+1):
            if pointer<len(nums):
                if i == nums[pointer]:
                    pointer+=1
                    continue
            res.append(i)
        return res
