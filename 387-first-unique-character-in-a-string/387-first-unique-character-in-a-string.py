class Solution:
    def firstUniqChar(self, s: str) -> int:
        lookup = {}
        for i in s:
            if i in lookup.keys():
                lookup[i] = lookup[i]+1 
            else:
                lookup[i] = 1
        for index,value in enumerate(s):
            if lookup[value] == 1:
                return index
        return -1