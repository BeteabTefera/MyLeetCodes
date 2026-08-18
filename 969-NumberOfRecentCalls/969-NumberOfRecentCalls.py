# Last updated: 8/18/2026, 2:49:28 PM
class RecentCounter(object):

    def __init__(self):
        self._counter = 0
        self._requests_time = []
        self._ptr = None

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
            # The first ping
        if not self._requests_time:
            self._ptr = 0
            self._counter = 1
        else:
            self._counter += 1

        self._requests_time.append(t)
        min_range = max(0, t - 3000)
        
        # check out of range
        while self._ptr < len(self._requests_time) and self._requests_time[self._ptr] < min_range:
            self._ptr += 1
            self._counter -= 1

        return self._counter


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)