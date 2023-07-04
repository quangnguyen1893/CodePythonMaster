val = []
wt = []
n, W = map(int, input().split())
# print(n,W)
items = [(0, 0) for i in range(n + 1)]
for i in range(1, n + 1):
    items[i] = input().split()
    val.append(items[i][1])
    wt.append(items[i][0])

t = [[-1 for i in range(W + 1)] for j in range(n + 1)]

def knapsack(wt, val, W, n):
    # base conditions
    if n == 0 or W == 0:
        return 0
    if t[n][W] != -1:
        return t[n][W]
    # choice diagram code
    if int(wt[n - 1]) <= W:
        t[n][W] = max(
            int(val[n - 1]) + knapsack(
                wt, val, W - int(wt[n - 1]), n - 1),
            knapsack(wt, val, W, n - 1))
        return t[n][W]
    elif int(wt[n - 1]) > W:
        t[n][W] = knapsack(wt, val, W, n - 1)
        return t[n][W]

print(knapsack(wt, val, W, n))

