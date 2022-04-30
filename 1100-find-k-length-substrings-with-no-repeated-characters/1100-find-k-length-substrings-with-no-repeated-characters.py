class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        l=0
        r=k
        output = 0
        while l!=len(s)-(k-1):
            cur = s[l:r]
            if len(list(cur)) == len(set(cur)):
                output+=1
            l+=1
            r+=1
        return output