# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        que = collections.deque()
        que.append((root, -float('inf')))
        total = 0
        while que:
            node, currMax = que.popleft()
            if node.val >= currMax:
                total += 1
                currMax = node.val
            if node.left:
                que.append((node.left, currMax))
            if node.right:
                que.append((node.right, currMax))
            
        return total
            
        


        