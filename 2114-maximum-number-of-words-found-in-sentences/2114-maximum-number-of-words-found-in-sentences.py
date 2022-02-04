class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        res = 0
        for i in sentences:
            res = max(len(i.split()),res)
        return res