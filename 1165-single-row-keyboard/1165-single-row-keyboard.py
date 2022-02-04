class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        lookup = {}
        total=0
        for count,value in enumerate(keyboard):
            lookup[value] = count
        prev = 0 
        for i in word:
            total += abs(lookup.get(i) - prev)
            prev = lookup.get(i)
        return total
