class Solution(object):
    def removeElement(self, nums, val):
        """
            U: must use inplace removal, so no creating another array. 
            M: array problem
            P: 
                - plan to count the number of occurence of val element using array.count() and loop for that range and remove the val
        """
        for i in range(nums.count(val)):
            nums.remove(val)
        
        return len(nums)