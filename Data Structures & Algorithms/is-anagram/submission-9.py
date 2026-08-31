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
        # return Counter(s) == Counter(t)
        if len(s) != len(t):
            return False
        hashmapS, hashmapT = {}, {}
        for i in range(len(s)):
            hashmapS[s[i]] = 1 + hashmapS.get(s[i], 0)
            hashmapT[t[i]] = 1 + hashmapT.get(t[i], 0)
        return hashmapS == hashmapT


















        if len(s) != len(t):
            return False
        hashS, hashT = {}, {}
        for i in range(len(s)):
            hashS[s[i]] = hashS.get(s[i], 0) + 1
            hashT[t[i]] = hashT.get(t[i], 0) + 1
        for i in hashS:
            if hashS[i] != hashT.get(i,0):
                return False
        return True
        