class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        left = 0
        right = 0
        seen = {}
        while right < len(s):
            if s[right] in seen and seen[s[right]] >= left:
                left = seen[s[right]] + 1
            length = max(length,right - left +1)
            seen[s[right]] = right
            right+=1
        return length