class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        highest=sum(accounts[0])
        for i in accounts:
            if sum(i) > highest:
                highest = sum(i)
        return highest