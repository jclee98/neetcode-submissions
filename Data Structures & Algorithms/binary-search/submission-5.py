'''
Two pointer method, L and R
Get the mid point
While L <= R
    if target > value at L, replace L with mid + 1
    if target < value at R, replace R with mid - 1
    if value at mid point equals to the target, return mid
    increment and decrement L and R espectively
return -1
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L = 0
        R = len(nums) - 1
        while L <= R:
            mid = (L + R) // 2
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                L = mid + 1
            elif target < nums[mid]:
                R = mid - 1
        return -1
            
