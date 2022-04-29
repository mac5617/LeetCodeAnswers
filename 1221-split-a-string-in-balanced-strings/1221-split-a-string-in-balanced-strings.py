class Solution:
    def balancedStringSplit(self, s: str) -> int:
        ret = count = 0
        for i in s:
            if i == 'L':
                count+=1
            else:
                count-=1
            if not count:
                ret+=1
        return ret