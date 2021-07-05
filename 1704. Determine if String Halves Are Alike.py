class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        half = len(s)//2
        a = s[:half].lower()
        b = s[half:].lower()
        acount = 0
        bcount = 0
        vowel = ('a', 'e', 'i', 'o', 'u')
        for i in vowel:
            if i in a:
                acount+=a.count(i)
            if i in b:
                bcount+=b.count(i)
        return acount == bcount