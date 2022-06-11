class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password) < 8:
            return False
        hasLower = False
        hasUpper = False
        hasDigit = False
        hasSpecial = False 
        for i in range(len(password)):
            if i > 0:
                if password[i] == password[i-1]:
                    return False
            if password[i].islower():
                hasLower=True
            elif password[i].isupper():
                hasUpper=True
            elif password[i].isdigit():
                hasDigit=True
            elif password[i] in "!@#$%^&*()-+":
                hasSpecial = True
        if hasLower and hasUpper and hasDigit and hasSpecial:
            return True