class Solution:
    def intToRoman(self, num: int) -> str:
        numerals = {
            1000:'M',
            900:'CM',
            500:'D',
            400:'CD',
            100:'C',
            90:'XC',
            50:'L',
            40:'XL',
            10:'X',
            9:'IX',
            5:'V',
            4:'IV',
            1:'I',  
        }
        result = []
        for key,value in numerals.items():
            while num >0:
                if key <= num:
                    num-=key
                    result.append(value)
                else: 
                    break
        return ''.join(result)
first = Solution()
print(Solution.intToRoman(125))