class Solution:
    def convert(self,s: str, numRows: int) -> str:
        seen = {}
        count = 1
        full = False
        if numRows == 1:return s
        for i in s:
            if full == True:
                if count == 1:
                    full = False
                else:
                    cur = seen[count]
                    seen[count] = cur + i
                    count-=1
            if full == False:
                # gets the first three iterations
                if seen.get(count) == None:
                    seen[count] = i
                    if count != numRows:
                        count+=1
                    else:
                        count-=1
                        full=True
                    continue
                if count == numRows:
                    full = True
                    cur = seen[count]
                    seen[count] = cur + i
                    count-=1
                else:
                    cur = seen[count]
                    seen[count] = cur + i
                    count+=1
        return ''.join(seen.values())
