class Solution:
    def largestGoodInteger(self, num: str) -> str:
        big = -1
        if num == f'{num[0]}{num[0]}{num[0]}':
            return f'{num[0]}{num[0]}{num[0]}'
        for i in range(len(num)-2):
            cur = num[i:i+3]
            if cur == f'{num[i]}{num[i]}{num[i]}':
                if int(num[i]) > big:
                    big = int(num[i])
        if big != -1:
            return f'{big}{big}{big}'
        else: 
            return ''