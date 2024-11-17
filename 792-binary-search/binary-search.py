class Solution(object):
    def search(self, nums, target):
        """
        Understand: 
            - oh okay so this is quite easy
            - Given:
                - nums in ascending order
                - return the target index
        """

        #Brute force
        if target not in nums:
            return -1
        else:
            return nums.index(target)
