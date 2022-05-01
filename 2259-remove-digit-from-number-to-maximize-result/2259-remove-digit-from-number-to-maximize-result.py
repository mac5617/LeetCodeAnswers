class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        tracker = []
        for index,value in enumerate(number):
            cur = list(number)
            if value == digit:
                cur.pop(index)
                tracker.append(int(''.join(cur)))
        return str(max(tracker))