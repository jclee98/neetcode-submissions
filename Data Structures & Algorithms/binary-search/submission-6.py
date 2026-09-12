'''
Two pointer method, L and R
Get the mid point
While L <= R
    if target > value at mid, replace L with mid + 1
    if target < value at mid, replace R with mid - 1
    if value at mid point equals to the target, return mid
    increment and decrement L and R espectively
return -1
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L, R = 0, len(nums) - 1
        while L <= R:
            mid = (L+R)//2
            if target == nums[mid]:
                return mid
            if target < nums[mid]:
                R = mid - 1
            if target > nums[mid]:
                L = mid + 1
        return -1 
            
