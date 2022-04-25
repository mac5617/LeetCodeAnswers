class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ret = []
        for i in nums:
            ret.append(i*i)
        return sorted(ret)