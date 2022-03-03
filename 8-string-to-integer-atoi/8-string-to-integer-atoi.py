class Solution:
    def myAtoi(self, s: str) -> int:
        negative = False
        number = ''
        s = s.lstrip()
        passover = 0
        if len(s)==0: return 0
        if s[0] == '-' or s[0] == '+':
            passover = 1
            if s[0] == '-':
                negative = True
        for i in range(len(s)):
            if passover == 1 and i == 0:
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