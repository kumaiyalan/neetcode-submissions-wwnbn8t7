class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        valid = []

        def backtrack(openP, closedP, path):
            if openP == closedP == n:
                valid.append(path)
                return
            if openP < n:
                backtrack(openP + 1, closedP, path + '(')
            if closedP < openP:
                backtrack(openP, closedP + 1, path + ')')
        
        backtrack(0, 0, '')
        return valid


