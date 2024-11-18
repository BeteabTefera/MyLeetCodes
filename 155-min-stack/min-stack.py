class MinStack(object):
    #doing it now using one stack and tuples
    def __init__(self):
        self.stack = []

    def push(self, val):
        if self.stack and self.stack[-1][1] < val:
            self.stack.append((val, self.stack[-1][1]))
        else:
            self.stack.append((val, val))

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()

        
    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        return  self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()