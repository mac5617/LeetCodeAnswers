class Solution:
    def reverseWords(self, s: str) -> str:
        rev = [words[::-1] for words in s.rsplit()]
        return ' '.join(rev)