class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        lookup = {}
        for curr in nums:
            if len(nums) < 2:
                return False
            if lookup.get(curr):
                lookup[curr] = lookup.get(curr) + 1
                if lookup.get(curr) > 1:
                    return True
            else:
                lookup.update({curr: 1})
        return False