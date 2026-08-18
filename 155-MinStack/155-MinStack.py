# Last updated: 8/18/2026, 2:50:22 PM
class MinStack(object):

    def __init__(self):
        self.arr = []
        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.arr.append(val)
        

    def pop(self):
        """
        :rtype: None
        """
        self.arr.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.arr[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return min(self.arr)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()