class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        left, right = 0 , len(nums) - 1
        while left <= right:
            if nums[left] == val:
                # Swap with the element at the 'right' pointer
                nums[left], nums[right] = nums[right], nums[left]
                # Decrement the 'right' pointer
                right -= 1
            else:
                # Increment the 'left' pointer if the element is valid
                left += 1

        return left