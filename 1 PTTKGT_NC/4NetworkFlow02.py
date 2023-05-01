# A và B làm ở các dự án khác nhau. Họ cần thực hiện một số lô các tiến trình.
# Một lô gồm nhiều tiến trình, ở đó các tiến trình cần một số máy để thực thi.
# Một máy chỉ có thể thực thi các tiến trình của A hoặc của B.
# A được giao thực hiện các lô của anh.
# Bộ phận quản lý nhận thấy tổng số tiến trình có thể thực hiện trên các máy có thể được
# tăng lên tối đa nếu để B thay thế một số hoặc tất cả các tiến trình của A.
# Tính số tiến trình mà B cần thực hiện để tổng số tiến trình thực thi trên các máy là tối đa.
#
# Lưu ý
# Một máy có thể thực hiện các tiến trình từ các lô khác nhau, nhưng chỉ xuất phát từ 1 người, hoặc của A hoặc của B.
# Các tiến trình của A đang thực hiện trên các máy. B muốn thực thi các lô tiến trình của mình để tổng số tiến trình thực hiện
# trên tất cả các máy là có thể tăng thêm. Một lô của B có thể thực hiện tất cả các tiến trình bên trong hoặc không thực thi tiến
# trình nào.
# Nếu B thay một máy với các tiến trình của mình thì các tiến trình của các lô khác của anh ấy có thể đựợc thực hiện trên máy đó.
# Một lô cần s máy để thực hiện và gồm p tiến trình bên trong.
#
# Đầu vào
#
# Dòng đầu tiên là 1 số nguyên n  - số lượng máy,
# Dòng kế tiếp gồm n số nguyên Si cách nhau khoảng trắng, số lượng tiến trình của A đang thực thi trên máy thứ i.
# Dòng kế tiếp là một số nguyên b - số lượng lô của B
# b dòng kế tiếp, mỗi dòng đại diện cho 1 lô của B, gồm các số nguyên cách nhau khoảng trắng. Số đầu tiên là s - số lượng máy mà lô đó cần; theo sau là s số nguyên, mỗi số chỉ số hiệu máy; cuối cùng là 1 số nguyên p chỉ số lượng tiến trình mà lô đó cần thực hiện.
# Đầu ra:
# 1 số nguyên là tổng số tiến trình B đặt vào để thay thế một số tiến trình của A trên một số hoặc tất cả các máy.
# Chú ý:
# Bạn có thể an tâm rằng dữ liệu đầu vào luôn hợp lệ
# Ràng buộc
#
# 1 <= n <= 100
# 0 <= Si <=  70
# 0 <= b <100
# 1 <= p <=50
# Giải thích ví dụ
#
# Ví dụ 1: B có thể thực thi các tiến trình của lô 1 bằng cách thay thế các tiến trình của A ở máy 1, 2, 3.
# Tuy nhiên, B có thể thực hiện các tiến trình của lô 2 trên máy 3 và 4; lúc đó các tiến trình của A trên máy 4 cũng được thay thế.
# Tổng số có 26 tiến trình được thực hiện so với 25 tiến trình ban đầu.
# Ví dụ 2: B có thể thực thi các tiến trình của lô 2 bằng cách thay thế các tiến trình của A trên máy 2 và 3;
# cộng với thực thi các tiến trình của lô 3 bằng cách thay các tiến trình của A trên máy 4.
# Số lượng tiến trình đang thực thi được tăng lên là 2.

from collections import defaultdict
def solution2(a, b):
    visited = set()
    p_total = 0
    res = -9999
    for i in b.items():
        for j in i[1]['path']:
            visited.add(j)
        count_A = 0
        for k in visited:
            count_A += a[k]
        p_total += i[1]['p']
        if p_total - count_A >= res:
            res = p_total - count_A
    return res
if __name__ == '__main__':
    # number of machines
    n = int(input())
    s_i = input().split()
    A_dict = defaultdict(int)
    for i, value in enumerate(s_i, 1):
        A_dict[i] = int(value)
    B_dict = {}
    b = int(input())
    for i in range(1, b + 1):
        b_i = input().split()
        path = [int(value) for value in b_i[1:1 + int(b_i[0])]]
        x = 0
        for j in path:
            x += A_dict[j]
        B_dict[i] = {
            'path': path,
            'a_val': -x,
            'p': int(b_i[-1])
        }
    # Sort B desc
    B_dict = {k: v for k, v in sorted(B_dict.items(), key=lambda item: (item[1]['p'], item[1]['a_val']), reverse=True)}
    print(solution2(A_dict, B_dict))