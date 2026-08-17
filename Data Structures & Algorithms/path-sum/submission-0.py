# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        total = 0
        def dfs(root, total):
            if not root:
                return False
            total += root.val
            if total == targetSum and root.left is None and root.right is None:
                return True
            if dfs(root.left, total):
                return True
            if dfs(root.right, total):
                return True
            total -= root.val
            return False
        return dfs(root, 0)