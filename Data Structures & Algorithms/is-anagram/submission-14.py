'''
check if length is the same

create hashmap for eaech string to store each char's count

populate hashmap by iterating the string and adding 1, use .get(x, 0)

for each val in first compare with the val in the other one

OR

just simply return counter(s) == counter(t)
'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        hashmapS, hashmapT = {},{}
        for i in s:
            hashmapS[i] = 1 + hashmapS.get(i, 0)
        for i in t:
            hashmapT[i] = 1 + hashmapT.get(i, 0)
        for i in s:
            if hashmapS[i] != hashmapT.get(i,0):
                return False
        return True



















        