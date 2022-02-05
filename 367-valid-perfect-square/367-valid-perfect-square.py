class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        counter = 1
        ans = 0
        while ans<= num:
            ans = counter * counter
            if ans == num:
                return True
            elif ans < num:
                counter+=1
                continue
            else:
                return False