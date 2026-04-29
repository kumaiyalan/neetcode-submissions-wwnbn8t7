class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        
        left, right = 0, 0
        need = len(countT)
        have = 0
        res, resLen = [-1, -1], float("inf")

        while right < len(s):
            curr = s[right]
            if curr in countT:
                window[curr] = 1 + window.get(curr, 0)
                if window[curr] == countT[curr]:
                    have += 1
            
            while have == need:
                if (right - left + 1) < resLen:
                    res = [left, right]
                    resLen = (right - left + 1)
                delete = s[left]
                if delete in countT:
                    window[delete] -= 1
                    if window[delete] < countT[delete]:
                        have -= 1
                left += 1
            
            right += 1
        
        if resLen != float("inf"):
            return s[res[0] : res[1] + 1]
        else:
            return ""  