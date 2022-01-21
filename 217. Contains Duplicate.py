class SolutionOne:
    def containsDuplicate(nums: list[int]) -> bool:
        lookup = {}
        for curr in nums:
            if len(nums) < 2:
                return False
            if lookup.get(curr):
                lookup[curr] = lookup.get(curr) + 1
                if lookup.get(curr) > 1:
                    return True
            else:
                lookup.update({curr: 1})
        return False



class SolutionTwo:
    def containsDuplicate(nums: list[int]) -> bool:
        lookup = set()
        for curr in nums:
            if curr in lookup:
                return True
            else:
                lookup.add(curr)
        return False


print(SolutionOne.containsDuplicate(nums=[1, 2, 3, 1, 4, 5, 6, 7, 1, ]))
print(SolutionTwo.containsDuplicate(nums=[1, 2, 3, 1, 4, 5, 6, 7, 1, ]))
