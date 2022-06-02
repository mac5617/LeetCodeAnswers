class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        out = []
        for curr in range(len(matrix[0])):
            temp = []
            for currin in range(len(matrix)):
                temp.append(matrix[currin][curr])
            out.append(temp)
        return out