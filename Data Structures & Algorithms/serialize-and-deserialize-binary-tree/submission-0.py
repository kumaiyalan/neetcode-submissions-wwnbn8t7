# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:

    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        preorder = []
        def dfs(root):
            if not root:
                preorder.append('#')
                return
            preorder.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        res = ",".join(preorder)
        print(res)
        return res


    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        nodes = data.split(',')
        nodes = collections.deque(nodes)
        def build(nodes):
            node = nodes.popleft()
            if node == '#':
                return 
            root = TreeNode(int(node))
            root.left = build(nodes)
            root.right = build(nodes)
            return root
        return build(nodes)
