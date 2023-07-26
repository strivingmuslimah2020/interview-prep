class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        
        dp = [[0 for col in range(cols)] for row in range(rows)]
        dp[0][0] = grid[0][0]
        
        for row in range(rows):
            for col in range(cols):
                
                if row == 0 and col > 0:
                    dp[row][col] = grid[row][col] + dp[row][col - 1]
                elif col == 0 and row > 0:
                    dp[row][col] = grid[row][col] + dp[row - 1][col]
                elif col > 0 and row > 0:
                    dp[row][col] = min(dp[row][col - 1], dp[row - 1][col]) + grid[row][col]
                
        return dp[-1][-1]