MOD = 10**9 + 7

n, m = map(int, input().split())

# 创建 dp 数组，确保有足够的行和列
dp = [[0] * (m + 1) for _ in range(n + 1)] 
#n是行数，m是列数

# 初始化第一行和第一列
for i in range(1, n + 1):
    dp[i][1] = 1
for j in range(1, m + 1):
    dp[1][j] = 1

# 动态规划填表
for i in range(2, n + 1):
    for j in range(2, m + 1):
        dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % MOD

# 输出结果
print(dp[n][m])
#使用了动态规划