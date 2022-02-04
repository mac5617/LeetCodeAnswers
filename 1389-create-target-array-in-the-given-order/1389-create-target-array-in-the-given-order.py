class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        # index[0]  0 0 [0]
        # index[1]  1 1 [01]
        # index[2]  2 2 [012]
        # index[3]  2 3 [0132]
        # index[4]  1 4 [04132]
        res = []
        for i in range(len(nums)):
            res.insert(index[i],nums[i])
        return res