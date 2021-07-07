class Solution:
    def countConsistentStrings(self, allowed: str, words: list[str]) -> int:
            count=0
            for i in words:
                for j in range(len(i)):
                    if i[j] not in allowed:
                        break
                    if (len(i)-1) == j:
                        count+=1
            return count
                    