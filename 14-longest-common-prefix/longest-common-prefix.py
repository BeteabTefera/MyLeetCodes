
class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:  # Handle empty input list
            return ""
        
        prefix = strs[0]  # Start with the first string as the prefix
        
        for s in strs[1:]:
            # Reduce the prefix until it matches the current string
            while not s.startswith(prefix):
                prefix = prefix[:-1]  # Remove the last character from the prefix
                if not prefix:  # If prefix becomes empty, return
                    return ""
        
        return prefix

            