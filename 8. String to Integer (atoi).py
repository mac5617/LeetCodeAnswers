class Solution:
    def myAtoi(self, s: str) -> int:
        negative = False
        number = ''
        s = s.lstrip()
        for i in range(len(s)):
            if s[i] == '-' or s[i] == '+':
                if i != 0:
                    break
                if s[i] == '-':
                    negative = True
                continue
            if s[i].isdigit()!=True:
                break
            number+=s[i]
        if len(number) == 0:
            return 0
        number = int(number)
        if negative == True:
            number = number * -1
        if number < -2147483648: 
            number = -2147483648
        if number > 2147483647:
            number = 2147483647
        return number