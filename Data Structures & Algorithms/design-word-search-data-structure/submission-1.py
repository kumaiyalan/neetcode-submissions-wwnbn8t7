class WordDictionary:

    def __init__(self):
        self.children = {}
        self.word = False
        

    def addWord(self, word: str) -> None:
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = WordDictionary()
            curr = curr.children[c]
        curr.word = True
        

    def search(self, word: str) -> bool:
        curr = self
        for i in range(len(word)):
            if word[i] == '.':
                for child in curr.children.values():
                    if child.search(word[i + 1:]):
                        return True
                return False
            if word[i] not in curr.children:
                return False
            curr = curr.children[word[i]]
        return curr.word