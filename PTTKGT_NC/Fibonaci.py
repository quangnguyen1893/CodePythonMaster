def F(n, memo = {}):
    if n in memo:
        return memo[n]
    if n<=2:
        f = n
    else:
        f = F(n-1)+F(n-2)
    memo[n]=f
    return f
n = int(input())
for i in range(1,n+1):
    print(F(i), end=" ")

