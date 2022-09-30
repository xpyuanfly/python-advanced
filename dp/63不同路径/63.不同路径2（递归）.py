class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        d = {}

        def dfs(i, j):
            if (i, j) in d:
                return d[i, j]
            # 边界/障碍物检查
            if i < 0 or j < 0 or obstacleGrid[i][j] == 1:
                return 0
            # 达到终点了
            if i == 0 and j == 0:
                return 1
            # 继续往左(i,j-1)、往上(i-1,j)递归调用
            d[i, j] = dfs(i - 1, j) + dfs(i, j - 1)
            return d[i, j]

        print(dfs(m - 1, n - 1))
        # print(obstacleGrid[0][1])
        # print(type(obstacleGrid[0][1]))


solution = Solution
solution().uniquePathsWithObstacles([[0, 0, 0],
                                     [0, 1, 0],
                                     [0, 0, 0]])
