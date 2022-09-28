class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        dp = [[0] * m for _ in range(n)]
        # (0,0)这个格子可能有障碍物
        dp[0][0] = 0 if obstacleGrid[0][0] else 1
        # 处理第一列
        for i in range(1, n):
            if obstacleGrid[i][0] == 1 or dp[i - 1][0] == 0:
                dp[i][0] = 0
            else:
                dp[i][0] = 1
        # 处理第一行
        for j in range(1, m):
            if obstacleGrid[0][j] == 1 or dp[0][j - 1] == 0:
                dp[0][j] = 0
            else:
                dp[0][j] = 1

        for i in range(1, n):
            for j in range(1, m):
                # 如果当前格子是障碍物
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                # 路径总数来自于上方(dp[i-1][j])和左方(dp[i][j-1])
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        print(dp[-1][-1])


solution = Solution
solution().uniquePathsWithObstacles([[0, 0, 0],
                                     [0, 1, 0],
                                     [0, 0, 0]])
