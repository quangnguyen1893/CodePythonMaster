# Có n công việc (yêu cầu) cần thực hiện trên 1 máy (tài nguyên).
# Mỗi công việc có thời gian bắt đầu si và thời gian kết thúc là fi.
# 2 công việc i, j gọi là tương thích nhau nếu chúng không chồng lấn nhau, tức fi <= sj hay fj <= si
#
# Hỏi số lượng công việc tương thích lớn nhất là bao nhiêu?
#
# Đầu vào:
# Dòng đầu tiên là số nguyên n: số công việc
# Dòng kế tiếp gồm n số nguyên, số nguyên thứ i, ký hiệu si là thời gian bắt đầu của công việc
# Dòng kế tiếp gồm n số nguyên, số nguyên thứ i, ký hiệu fi là thời gian kết thúc của công việc i.
#
# Đầu ra:
# Một số nguyên là số lượng tối đa công việc có thể thực hiện được
# 0 1 2 3 3 5 5 6 7 8
# 4 2 4 5 6 6 7 7 9 10

def interval_scheduling(stimes, ftimes):
    index = list(range(len(stimes)))
    index.sort(key=lambda i: ftimes[i])
    maximal_set = set()
    prev_finish_time = 0
    for i in index:
        if stimes[i] >= prev_finish_time:
            maximal_set.add(i)
            prev_finish_time = ftimes[i]
    return maximal_set

n = int(input())
stimes = input().split()
stimes = [int(st) for st in stimes]
ftimes = input().split()
ftimes = [int(ft) for ft in ftimes]
ans = interval_scheduling(stimes, ftimes)
print(len(ans))