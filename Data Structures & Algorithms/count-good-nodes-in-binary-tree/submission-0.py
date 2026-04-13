# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        maxSeen = root.val
        goodNodes = 0

        stack = [(root, root.val)]

        while stack:
            node, currentMax = stack.pop()
            if node.val >= currentMax:
                goodNodes += 1

            newMax = max(currentMax, node.val)
            if node.left:
                stack.append((node.left, newMax))
            if node.right:
                stack.append((node.right, newMax))

        return goodNodes
        