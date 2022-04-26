class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        lookup = {}
        for i in range(len(arr1)):
            if arr1[i] in lookup:
                lookup[arr1[i]]+=1
            else:
                lookup[arr1[i]]=1
            if arr2[i] in lookup:
                lookup[arr2[i]]+=1
            else:
                lookup[arr2[i]]=1
            if arr3[i] in lookup:
                lookup[arr3[i]]+=1
            else:
                lookup[arr3[i]]=1
        return [key for key,value in lookup.items() if value == 3]