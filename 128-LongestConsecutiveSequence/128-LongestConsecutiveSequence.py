# Last updated: 8/18/2026, 2:50:29 PM
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #base case:
        if not nums:
            return 0
        #vars
        num_set = set(nums)
        max_count = 0

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_count = 1

                while current_num +1 in num_set:
                    current_num += 1
                    current_count += 1
                
                max_count = max(max_count, current_count)
        return max_count    