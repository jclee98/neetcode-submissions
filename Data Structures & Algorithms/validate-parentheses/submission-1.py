class Solution:
    def isValid(self, s: str) -> bool:
        dictCT = {')':'(', ']':'[', '}':'{'}
        stack = []
        for i in s:
            if i not in dictCT:
                stack.append(i)
            else:
                if not stack:
                    return False
                else:
                    popped = stack.pop()
                    if popped != dictCT[i]:
                        return False
        return not stack 
        