# Last updated: 8/18/2026, 2:49:57 PM
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
