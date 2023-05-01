# Một công ty sản xuất hai loại sản phẩm: loại tiêu chuẩn A và loại đặc biệt B. Chi phí cho một
# sản phẩm A là pA và chi phí cho một sản phẩm B là pB. Công ty bán qA sàn phẩm A và qB sản phẩm B yới
# qA = 400-2pA + pB
# qB = 200 + pA-pB
# Để sản xuất 1 sản phẩm A cần 2 giờ công lao động và 1 kg nguyên liệu thô.
# Sản xuất 1 sản phấm B cần 3 giờ công lao động và 2 kg nguyên liệu thô. Hiện tại công ty đang
# có đủ công nhân cho 1000 giờ công lao động và 200 kg nguyên liệu thô.
# Tim pA và pB sao cho công ty tối ưu hoá thu nhập.
# a.  Mô hình hoá bài toán
# b.  Giải bài toán bằng phương pháp Larange
# C.  Giải bằng thư viện CVXOPT
# Gợi ý: x2 + y2 + xy = [x  y][ 1     0.5   [x
#                               0.5   1]     y]
# Điều chỉnh các số trong ma trận sẽ có được vế trái như mong muốn