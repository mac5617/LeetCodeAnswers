class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        run_sum = []
        final_sum = []
        for i in range(len(nums)):
            run_sum.append(nums[i])
            final_sum.append(sum(run_sum))
        return final_sum