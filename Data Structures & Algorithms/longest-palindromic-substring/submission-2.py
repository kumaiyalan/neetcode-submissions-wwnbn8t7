class Solution:
    def longestPalindrome(self, s: str) -> str:
        left, right = 0, 0
        longest = 1
        res = s[0]

        for i in range(len(s)):
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
                length = (right - left + 1)
                if length > longest:
                    longest = length
                    res = s[left + 1:right]

            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
                length = (right - left + 1)
                if length > longest:
                    longest = length
                    res = s[left + 1:right]

        return res