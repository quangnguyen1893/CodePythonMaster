# Nhà hàng XYZ có thể chuẩn bị N hộp cơm trưa và phân phối cho các công ty đặt hàng.
# Có M công ty, công ty thứ i đặt Ai hộp cơm.
# Nhà hàng có thể từ chối đơn đặt hàng của công ty thứ i bất kỳ, hoặc nếu chấp nhận thì nhà hàng phải cung cấp đủ Ai hộp cơm.
# Tính số lương công ty tối đa mà nhà hàng có thể phục vụ.
#
# Đầu vào:
# Dòng đầu tiên là số nguyên T, số lượng test cases.
# Mỗi test case gồm 2 dòng
# Dòng đầu tiên là 2 số nguyên M, N là số lượng hộp cơm mà nhà hàng có thể phục vụ / số lượng công ty đặt; mỗi số cách nhau khoảng trắng.
# Dòng thứ 2 gồm N số nguyên Ai (i=1..N)
#
# Đầu ra:
# Mỗi test case in ra một số nguyên là số lượng công ty tối đa nhà hàng có thể phục vụ (số công ty nhận được hộp cơm).
# 2
# 10 4
# 3 9 4 2         3
# 5 6
# 3 2 1 1 2 1     4

def numberComServed(numBox_numComOrder, testCase):
    testCase.sort()
    coreTagert = 0
    maximal_set = []
    for i in range(len(testCase)):
        coreTagert += testCase[i]
        if coreTagert <= numBox_numComOrder[0]:
            maximal_set.append(testCase[i])
    return maximal_set


n = int(input())

for i in range(n):
    numBox_numComOrder = input().split()
    numBox_numComOrder = [int(st) for st in numBox_numComOrder]
    testCase = input().split()
    testCase = [int(ft) for ft in testCase]
    ans = numberComServed(numBox_numComOrder, testCase)
    print(len(ans))
