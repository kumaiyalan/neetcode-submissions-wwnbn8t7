class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match = {"}": "{", ")": "(", "]": "["}

        for i in range(len(s)):
            if s[i] in match:
                if stack == [] or stack[-1] != match[s[i]]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(s[i])
        
        return stack == []