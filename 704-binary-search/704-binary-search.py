class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while(left<=right):
            mid = (left + right) // 2
            point = nums[mid]
            if point == target:
                return mid
            elif point < target:
                left = mid + 1
            elif point > target:
                right = mid - 1
        return -1