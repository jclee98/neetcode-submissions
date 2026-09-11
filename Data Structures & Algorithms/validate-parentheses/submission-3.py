'''
Create a dict to store the closing bracket to its opening bracket

Create a stack

Iterate the brackets 
    if it is a open, add to the stack. 
    Else, 
        if stack is empty, return false.
        else, check if the opening popped value matches the close in the dict, false if it not
lastly, check if the stack is empty, by returning not stack
    
'''
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