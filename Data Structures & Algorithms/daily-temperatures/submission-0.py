class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if len(temperatures) == 1:
            return [0]
        res = [0] * len(temperatures)
        stack = [(0, temperatures[0])]

        for i, temp in enumerate(temperatures):
            if temp <= stack[-1][1]:
                stack.append((i, temp))
            else:
                while stack and temp > stack[-1][1]:
                    res[stack[-1][0]] = i - stack[-1][0]
                    stack.pop()
                stack.append((i, temp))
        return res