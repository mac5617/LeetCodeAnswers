class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":return []
        keypad = {
                  '2':['a','b','c'],
                  '3':['d','e','f'],
                  '4':['g','h','i'],
                  '5':['j','k','l'],
                  '6':['m','n','o'],
                  '7':['p','q','r','s'],
                  '8':['t','u','v'],
                  '9':['w','x','y','z']}

        seen = ['']
        for i in digits:
            temp = []
            for j in seen:
                for x in keypad[i]:
                    temp.append(j+x)
            seen=temp
        return seen
