class Solution:
    def minimumSum(self, num: int) -> int:
        res = [x for x in str(num)]
        res = sorted(res)
        return int(res[0] + res[2]) + int(res[1]+res[3])
        