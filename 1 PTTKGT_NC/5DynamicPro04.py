dp = []

def MaximumPathUtil(i, j, grid):
    global dp
    if (i == 0 or j == 0):
        return 0
    if (dp[i][j] != -1):
        return dp[i][j]
    dp[i][j] = (MaximumPathUtil(i, j - 1, grid) + MaximumPathUtil(i - 1, j, grid) - MaximumPathUtil(i - 1, j - 1,
                                                                                                    grid)) + int(
        grid[i - 1][j - 1])
    return dp[i][j]

m, n = map(int, input().split())
dp = [[-1 for i in range(m + 1)] for j in range(n + 1)]
a = [[0] * n for _ in range(m)]
for i in range(m):
    a[i] = list(input().split())
q = int(input())
while (q > 0):
    x, y = map(int, input().split())
    print(MaximumPathUtil(x, y, a))
    q = q - 1