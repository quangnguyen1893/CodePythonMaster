# Có n viên sỏi, viên sỏi thứ i có trọng lượng wi.
# Bạn tham gia một trò chơi như sau: Cứ mỗi lần bạn chọn 2 viên sỏi có trọng lượng lớn nhất và đập chúng vào nhau.
# Giả sử 2 viên nặng nhất có trọng lượng lần lượt là x và y với x<=y. Lúc đó kết quả của việc đập vào nhau là:
# Nếu x==y, cả hai viên bị phá hủy hoàn toàn
# Nếu x != y, viên sỏi x bị phá hủy hoàn toàn, viên sỏi còn lại có trọng lượng chỉ còn y-x.
# Kết thúc trò chơi, chỉ còn nhiều nhất 1 viên sỏi.
# Tính trọng lượng của viên sỏi còn lại, nếu không còn viên sỏi nào, kết quả trả về là 0
# Đầu vào
# Dòng đầu tiên là số nguyên n, số lượng viên sỏi
# Dòng kế tiếp gồm n số nguyên wi cách nhau khoảng trắng, trọng lượng từng viên sỏi
# Đầu ra
# Một số nguyên duy nhất là kết quả cần tìm.
# Ràng buộc
# 1<=  wi <= 106
# 1 <=n <= 105