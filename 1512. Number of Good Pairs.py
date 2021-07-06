def numIdenticalPairs(nums: list[int]) -> int:
    count = 0
    for i in range(len(nums)):
        print('I:', i,'Left: ',nums[i])
        for j in range(i+1,len(nums)):
            print('J:', j,'Right: ',nums[j])
            if nums[i] == nums[j] and i < j:
                count +=1
    return count
print(numIdenticalPairs([1,2,3,1,1,3]))