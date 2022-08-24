# 7
# 45 13 12 16 9 5 22
def DPmerge():
    n = int(input())
    nums = list(map(int, input().split()))
    # 构建二维数组，用无穷大值填充
    dp = [[float('inf')] * n for z in range(n)]

    # 合并自己的代价为0
    for i in range(n):
        dp[i][i] = 0
    # 构建列表用于存放花费的累积和，方便后面求sum[l][r]
    s = [0] * (n + 1)
    for i in range(1, n + 1):
        s[i] = s[i - 1] + nums[i - 1]

    for k in range(2, n + 1):
        for l in range(n - k + 1):
            r = l + k - 1
            for t in range(l, r):
                dp[l][r] = min(dp[l][t] + dp[t + 1][r], dp[l][r])
            # s[r + 1] - s[l]值即为sum[l][r]
            dp[l][r] += s[r + 1] - s[l]
    print(dp[0][n - 1])


DPmerge()