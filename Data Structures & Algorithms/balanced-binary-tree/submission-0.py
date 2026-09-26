# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced_check(self, root: Optional[TreeNode]) -> tuple:
        if not root:
            return (0, True)
        left = self.isBalanced_check(root.left)
        right = self.isBalanced_check(root.right)
        height = 1 + max(left[0], right[0])
        bool_check = left[1] and right[1] and abs(left[0] - right[0]) <= 1
        return (height, bool_check)
    
    def isBalanced(self, tup):
        return self.isBalanced_check(tup)[1]
        