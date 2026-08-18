# Last updated: 8/18/2026, 2:50:28 PM
class Solution:
    def isPalindrome(self, s: str) -> bool:
        formatted_str = ''.join([char.lower() for char in s if char.isalnum()])
        return True if formatted_str == formatted_str[::-1] else False