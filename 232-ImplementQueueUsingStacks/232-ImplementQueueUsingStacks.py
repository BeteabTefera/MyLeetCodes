# Last updated: 8/18/2026, 2:50:00 PM
class MyQueue(object):

    def __init__(self):
        self.mainstack = []
        self.stack2 = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        return self.mainstack.append(x)

    def pop(self):
        """
        :rtype: int
        """
        val = self.mainstack[0]
        self.mainstack = self.mainstack[1:]
        return val

    def peek(self):
        """
        :rtype: int
        """
        return self.mainstack[0]

    def empty(self):
        """
        """
        if len(self.mainstack) == 0:
            return True
        else:
             return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()