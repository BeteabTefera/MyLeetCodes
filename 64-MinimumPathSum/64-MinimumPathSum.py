# Last updated: 8/18/2026, 2:50:43 PM
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row, col = len(grid), len(grid[0])

        dp = [1000] * (col + 1)

        dp[1] = 0

        for i,j in product(range(row), range(col)):
            k = j + 1
            dp[k] = min(dp[k - 1], dp[k]) + grid[i][j]

        return dp[-1]