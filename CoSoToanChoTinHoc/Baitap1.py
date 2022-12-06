# 0.    Trước hết hãy import các module/hàm cần thiết, ví dụ import numpy as np
# from numpy.linalg import solve

# 1.	Sử dụng numpy.array, tạo 3 ma trận x, y và z như bên dưới
# x =(1 1 1) y=(3 2 1) z=(1
#                         1
#                         1)

# 2.	Tính tích hai ma trận xz, nếu không tính được giải thích lý do

# 3.	Tính yzx, nếu không tính được giải thích lý do

# 4.	Tính xzy, nếu không tính được giải thích lý do

# 5.	Tính (x + y)z, nếu không tính được giải thích lý do

# 6.	Tính (xz) + (yz), nếu không tính được giải thích lý do

# 7.	Sử dụng numpy.matrix làm lại các bài tập từ 1 đến 6

# 8.	Dùng numpy giải hệ phương trình tuyến sau   x + y = 3
#                                                   2x – 3y = 5

# 9.	Mô hình hoá bài toán bên dưới và dùng python để giải Công ty Ace Novelty muốn sản xuất 3 loại sản phẩm A, B và C.
# -	Để sản xuất được 1 sản phẩm A cần: 2 phút trên máy I, 1 phút trên máy II và 2 phút trên máy III.
# -	Để sản xuất được 1 sản phẩm B cần: 1 phút trên máy I, 3 phút trên máy II và 1 phút trên máy III
# -	Để sản xuất được 1 sản phẩm C cần: 1 phút trên máy I, 2 phút trên máy II và 2 phút trên máy III.
# Hiện nay, máy I có thể sử dụng được 3 giờ, máy II được 5 giờ và máy III được 4 giờ.
# Hỏi: có thể sản xuất được bao nhiêu sản phẩm loại A, loại B và loại C.
# Mô hình hoá bài toán về hệ phương trình tuyến tính. Sau đó dùng python để giải.
# Gợi ý: gọi x, y, z là số sản phẩm từng loại

# 10.	Mô hình hoá bài toán bên dưới và dùng python để giải
# Bộ phận quản lý tần số có nhiệm vụ theo dõi và hiện các nguồn phát sóng lạ.
# Để làm điều này họ sử dụng ba máy thu sóng đặt ở 3 vị trí khác nhau.
# Mỗi máy có khả năng phát hiện được hướng phát (đường thẳng đi từ nguồn phát đến máy thu) của một nguồn sóng.
# Để tìm được chính xác vị trí phát sóng, họ chỉ cần tìm giao điểm của 3 đường thẳng.
# Một ngày nọ, 3 máy thu sóng phát hiện được rằng có một sóng lạ được phát ra từ 1 vị trí (x,y) nào đó.
# Ba đường thẳng tương ứng thu được là:
# 2x – y = 2
# x + y = 5
# 6x – y = -5
# Hãy tìm xem vị trí của nguồn sóng nằm ở đâu ?
# Gợi ý:
# -	Điểm (x, y) chính là giao điểm của đường thẳng. Tuy nhiên 3 đường thẳng này không giao nhau 1 cùng 1 điểm, vì thế ta tìm giá trị gần đúng của điểm này.
# -	Sử dụng hàm lstsq (thay vì solve) để giải hệ phương trình.

#11.   Sử dụng Python để kiểm tra xem ma trận bên dưới có xác định dương không.
# A = (1  4   2
#      0  1   0
#      -1 -4  2)
# Gợi ý: tìm định thức của các ma trận con.

# 12.	Mô hình hoá bài toán và sử dụng numpy để giải
# Xét các điểm (x, y) trên vòng tròn tâm O(0, 0) bán kính 1. Với mỗi điểm (x, y), ta thực hiện phép biến đổi sau:
# x’ = 2x + y
# y’ = x + 4y
# Tìm điểm x, y trên vòng tròn, sao cho (x’)2 + (y’)2 lớn nhất.
# Gợi ý:
# -	Sử dụng dạng ma trận để viết lại các công thức
# -	Chuyển bài toán về bài toán tìm vector u = (x, y) sao cho ||z||2 lớn nhất với z là Au.
# Dùng python để viết chương trình tìm u = (x, y)




