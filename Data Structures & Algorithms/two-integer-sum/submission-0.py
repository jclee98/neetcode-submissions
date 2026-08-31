'''
use a hashmap to store each num and its indx

iterate through using enumerate to store

using diff = target - current_num, check if diff exists in the hashmap, if it does, return the soln.

if it doesn't then add that num and idx to the hashmap
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for idx, num in enumerate(nums):
            diff = target - num
            if diff in hashmap:
                return [hashmap[diff], idx]
            hashmap[num] = idx
    

        