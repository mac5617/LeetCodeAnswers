class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        seen = {}
        for index,value in enumerate(groupSizes):
            if value in seen:
                seen[value].append(index)
            else:
                seen[value] = [index]
        ret = []
        for key,value in seen.items():
            for j in range(len(value)//key):
                ret.append(value[j*key:j*key+key])
        return ret