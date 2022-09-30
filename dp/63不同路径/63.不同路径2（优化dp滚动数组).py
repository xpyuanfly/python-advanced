class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        dp = [0] * m
        # 起点可能有障碍物
        dp[0] = 1 if obstacleGrid[0][0] == 0 else 0

        for i in range(n):
            for j in range(m):
                # 有障碍物的格子直接赋0
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                # 否则dp[j]的值由左方和上一次迭代的dp[j]累加而来
                elif obstacleGrid[i][j] == 0 and j - 1 >= 0:
                    dp[j] = dp[j] + dp[j - 1]
        print(dp[-1])


solution = Solution
solution().uniquePathsWithObstacles([[0, 0, 0],
                                     [0, 1, 0],
                                     [0, 0, 0]])
