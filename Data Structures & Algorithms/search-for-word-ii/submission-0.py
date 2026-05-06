class Trie:
    def __init__(self):
        self.children = {}
        self.word = False

    def addWord(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = Trie()
            curr = curr.children[c]
        curr.word = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = Trie()
        for word in words:
            root.addWord(word)
        
        ROWS, COLS = len(board), len(board[0])
        res, path = set(), set()

        def dfs(r, c, node, word):
            if (r < 0 or c < 0 or
                r == ROWS or c == COLS or
                board[r][c] not in node.children or
                (r,c) in path):
                return

            path.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.word:
                res.add(word)
            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)
            path.remove((r,c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, '')
        
        return list(res)

