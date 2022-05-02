class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        sort = []
        for i in nums:
            if i % 2 == 0:
                sort.insert(0,i)
            else:
                sort.append(i)
        return sort