'''
two pointer method

L and R

while L < R
    check if char at L not isalnum(), + 1 and continue
    check if char at R not isalnum(), - 1 and continue
    check if char L lower() != char R lower(), return False
    increment L and decrement R
return True

'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        L = 0
        R = len(s) - 1
        while L < R:
            if not s[L].isalnum():
                L+=1
                continue
            if not s[R].isalnum():
                R-=1
                continue
            if s[L].lower() != s[R].lower():
                return False
            L+=1
            R-=1
        return True
























        # L = 0
        # R = len(s) - 1
        # while L < R:
        #     if not s[L].isalnum():
        #         L+=1
        #         continue
        #     if not s[R].isalnum():
        #         R-=1
        #         continue
        #     if s[L].lower() != s[R].lower():
        #         return False 
        #     L+=1
        #     R-=1
        # return True