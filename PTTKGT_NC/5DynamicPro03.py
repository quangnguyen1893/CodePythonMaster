# Có n hòn đá được xếp thẳng hàng từ trái sang phải. Một chú cóc đứng ở hòn đá thứ nhất.
# Mỗi bước nhảy từ hòn đá thứ i, chú có thể nhảy tối đa tới hòn đá thứ k  xa hơn (i+1, i+2, ..., i+k).
# Chú cóc không thể nhảy hơn hòn đá thứ n.
# Hỏi có bao nhiêu cách chú có thể nhảy tới hòn đá thứ n.
# Đầu vào:
# Gồm 2 số nguyên n và k, mỗi số cách nhau khoảng trắng
# Đầu ra:
# In ra kết quả ở modulo (109 + 7)
# Chú ý:
# Bạn có thể an tâm rằng dữ liệu đầu vào luôn hợp lệ
# Ràng buộc
# 1 <= n, k <= 104

def func2(n, k, d):
    d[0] = 1
    for i in range(1, n):
        idx = max(0, i - k)
        for j in range(idx, i):
            d[i] += d[j]
    return d[n - 1] % (10 ** 9 + 7)

n, k = input().split()
d = [0] * (int(n)+1)
print(func2(int(n),int(k),d))