class Solution:
    def checkValidString(self, s: str) -> bool:
        leftP = []
        stars = []
        for i in range(len(s)):
            if s[i] == '(':
                leftP.append(i)
            if s[i] == '*':
                stars.append(i)
            if s[i] == ')':
                if not leftP and not stars:
                    return False
                if not leftP:
                    stars.pop()
                else:
                    leftP.pop()
        if leftP == [] and stars == []:
            return True
        if len(leftP) > len(stars):
            return False
        while leftP:
            last = leftP.pop()
            closing = stars.pop()
            if last > closing:
                return False
        return True
            

        