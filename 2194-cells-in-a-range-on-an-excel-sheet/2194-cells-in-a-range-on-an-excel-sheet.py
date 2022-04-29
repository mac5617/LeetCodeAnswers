class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        l = s.rsplit(':')[0][0]
        r = s.rsplit(':')[1][0]
        n1=int(s.rsplit(':')[0][1:])
        n2=int(s.rsplit(':')[1][1:])
        output = []
        count = ord(r)-ord(l)
        for i in range(count+1):
            letter = chr(ord(l)+i)
            for i in range(n1,n2+1):
                output.append(f'{letter}{i}')
        return output