"""
0. Intuoition

1. What do tjhey wany?
- Bool 
- Do what
..

2. edge cases 

3. naive

4. Pattern 

5. Complexities 

"""


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for i in nums:
            if i not in hashset:
                hashset.add(i)
            else:
                return True
        return False














        # hashset = set()
        # for i in nums:
        #     if i not in hashset:
        #         hashset.add(i)
        #     else:
        #         return True
        # return False













    #     hashset = set()
    #     for n in nums:
    #         if n not in hashset:
    #             hashset.add(n)
    #         else:
    #             return True
    #     return False
        