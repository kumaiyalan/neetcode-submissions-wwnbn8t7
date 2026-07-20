class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token not in '+-*/':
                stack.append(token)
            else:
                y = int(stack.pop())
                x = int(stack.pop())
                if token == '+':
                    stack.append(x + y)
                if token == '-':
                    stack.append(x - y)
                if token == '*':
                    stack.append(x * y)
                if token == '/':
                    stack.append(x / y)
        
        return int(stack.pop())