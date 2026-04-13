# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def eq(root1, root2):
            if root1 is None and root2 is None:
                return True
            if root1 is None and root2 is not None:
                return False
            if root1 is not None and root2 is None:
                return False
            if root1.val != root2.val:
                return False
            
            return eq(root1.left, root2.left) and eq(root1.right, root2.right)
        
        que = collections.deque()

        que.append(root)

        while que:
            node = que.popleft()
            if eq(node, subRoot):
                return True
            if node.left:
                que.append(node.left)
            if node.right:
                que.append(node.right)
        
        return False
        
        