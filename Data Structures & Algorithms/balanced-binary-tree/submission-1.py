# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def isBalanced(self, root: Optional[TreeNode]) -> tuple:
        return self.check(root)[1]
    def check(self, q):
        if not q:
            return (0, True)
        left = self.check(q.left)
        right = self.check(q.right)
        height = 1 + max(left[0], right[0])
        bool_check = left[1] and right[1] and abs(left[0] - right[0]) <= 1
        return (height, bool_check)
        