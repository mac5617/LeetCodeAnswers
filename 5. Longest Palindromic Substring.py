class Solution:
    def longestPalindrome(self, s: str) -> str:
        def helper(l,r):
            while(l>=0 and r<len(s) and s[l] == s[r]):
                l-=1
                r+=1
            return s[l+1:r]
        ret = ''
        for i in range(len(s)):
            test = helper(i,i)
            if len(test) > len(ret):
                ret = test
            test = helper(i,i+1)
            if len(test) > len (ret):
                ret = test
        return ret
