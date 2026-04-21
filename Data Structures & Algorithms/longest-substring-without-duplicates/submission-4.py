class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == '':
            return 0
        if len(s) == 1:
            return 1
        maxSeq = 0
        left = right = 0
        seen = set()

        while right < len(s):
            maxSeq = max(maxSeq, right - left)
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            right += 1
        return max(maxSeq, len(seen)) 