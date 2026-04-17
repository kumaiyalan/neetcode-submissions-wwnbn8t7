class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastSeen = {}
        for i in range(len(s)):
            if s[i] in lastSeen:
                lastSeen[s[i]] = i
            else:
                lastSeen[s[i]] = i
        ans = []
        L = 0
        R = 0
        size = 0
        while L < len(s):
            R = max(R, lastSeen[s[L]])
            size += 1
            if L == R:
                ans.append(size)
                size = 0
            L += 1
        return ans

        