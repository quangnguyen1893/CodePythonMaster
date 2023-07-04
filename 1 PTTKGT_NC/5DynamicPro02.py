# Cho số nguyên N, tính giá trị N! MOD (109 + 7)
# Đầu vào:
# Dòng đầu tiên là số nguyên T, số lượng test cases.
# Mỗi test case là 1 số nguyên N
# Đầu ra:
# Với mỗi test case, in ra kết quả của N! MOD (109 + 7)
# Chú ý:
# Bạn có thể an tâm rằng dữ liệu đầu vào luôn hợp lệ
# Ràng buộc
# 1 <= T, N  <= 105


# def newMod(a,b):
#     res = a%b
#     return res if not res else res-b if a<0 else res
# def factorial(n):
#     M = 10**9 + 7
#     f = 1
#     for i in range(1, n + 1):
#         f = newMod(f * i,M)
#     return f
#
# s1 = int(input())
#
# for i in range(0,s1):
#     s2 = int(input())
#     print(factorial(s2))
def solution(n: int, d: dict):
    if n < 2:
        return 1
    if n not in d:
        d[n] = (n * solution(n - 1, d)) % (10 ** 9 + 7)
    return d[n]

d = {}
T = int(input())
for i in range(T):
    n = int(input())
    print(solution(n,d))