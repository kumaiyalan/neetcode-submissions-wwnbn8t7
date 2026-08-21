class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cache = {}

        def memo(index, curr):
            if index == len(s):
                return curr == ''
            if (index, curr) in cache:
                return cache[(index, curr)]
            newCurr = curr + s[index]
            res = memo(index + 1, newCurr)
            if newCurr in wordDict:
                res = res or memo(index + 1, '')
            cache[(index, curr)] = res
            return res
        return memo(0, '')