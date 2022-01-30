class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        expected = set(range(1,len(nums)+1))
        fixed = set(nums)
        res = expected - fixed
        return list(res)