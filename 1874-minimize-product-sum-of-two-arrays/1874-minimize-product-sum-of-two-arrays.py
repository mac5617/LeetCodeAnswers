class Solution:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        nums1 = sorted(nums1)
        nums2 = sorted(nums2,reverse=True)
        return sum([x*y for x,y in zip(nums1,nums2)])