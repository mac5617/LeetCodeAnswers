class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def checker(string):
            output = []
            for i in string:
                if i == '#':
                    if output:
                        output.pop()
                else: 
                    output.append(i)
            return ''.join(output)
        return checker(s) == checker(t)