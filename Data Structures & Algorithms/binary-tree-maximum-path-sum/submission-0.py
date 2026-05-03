# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = root.val

        def dfs(root):
            if root is None:
                return 0
            
            maxLeft = max(dfs(root.left), 0)
            maxRight = max(dfs(root.right), 0)
            self.res = max(self.res, maxLeft + root.val + maxRight)

            return root.val + max(maxLeft, maxRight)

        dfs(root)
        return self.res