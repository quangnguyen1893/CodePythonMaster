def enter(n, W, gems):
    n, W = map(int, input().split())

    gems = [(0, 0) for i in range(n + 1)]
    for i in range(1, n + 1):
        gems[i] = map(int, input().split())
    print(n, W, gems)
    return  n,W,gems

def trace_back(n, W, dp, gems):
    chosen_times = [0 for i in range(n + 1)]
    while W != 0:
        for i in range(1, n + 1):
            if dp[W] == dp[W - gems[i][0]] + gems[i][1]:
                W -= gems[i][0]
                chosen_times[i] += 1
                break

    print(chosen_times)


def solution(n, W, gems):
    dp = [0 for i in (W + 1)]
    for i in range(W + 1):
        for j in range(1, n + 1):
            if i >= gems[j][0]:
                dp[i] = max(dp[i], dp[i - gems[i][0]] + gems[i][1])
    print(dp[W])
    trace_back(n, W, dp, gems)


if __name__ == '__main__':
    n, W = 0, 0
    gems = []
    enter(n, W, gems)
    solution(n, W, gems)
