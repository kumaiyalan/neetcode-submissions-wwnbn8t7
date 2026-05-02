class Solution:
    def isPalindrome(self, s: str) -> bool:
        characters = ''
        for i in s:
            if i.isalnum():
                characters += i.lower()

        left = 0
        right = len(characters) - 1

        while left < right:
            if characters[right] != characters[left]:
                return False
            left += 1
            right -= 1
        return True