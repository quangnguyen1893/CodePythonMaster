import requests
from bs4 import BeautifulSoup
import os  # Thêm thư viện os

# Địa chỉ URL của trang web báo và chuyên mục bạn muốn crawl
base_url = "https://dantri.com.vn"
category_url = base_url + "/giao-duc.htm"  # Thay bằng URL chuyên mục thực tế

# Gửi yêu cầu HTTP để lấy trang web
response = requests.get(category_url)

# Kiểm tra xem yêu cầu có thành công không
if response.status_code == 200:
    # Sử dụng BeautifulSoup để phân tích HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # Tìm tất cả các thẻ liên quan đến bài báo, ví dụ như thẻ h3 với class "title-news"
    article_links = soup.find_all("h3", class_="article-title")  # Dantri

    # Lưu trữ thông tin về tiêu đề và URL của các bài báo
    articles_info = []

    # Kiểm tra xem tệp urls.txt có tồn tại hay không
    if not os.path.exists("/home/quang/CodePythonMaster/7 XuLiNNTuNhien/Bai4/urlsdantri.txt"):
        with open("/home/quang/CodePythonMaster/7 XuLiNNTuNhien/Bai4/urlsdantri.txt", "w", encoding="utf-8") as urls_file:
            # Tệp không tồn tại, viết dòng mô tả nếu cần
            urls_file.write("Các URL của bài viết:\n")

    # Mở tệp urls.txt để viết các URL vào đó
    with open("/home/quang/CodePythonMaster/7 XuLiNNTuNhien/Bai4/urlsdantri.txt", "a", encoding="utf-8") as urls_file:
        for link in article_links:
            article_url = link.a['href']
            article_title = link.a.text
            articles_info.append({"Tiêu đề": article_title, "URL": article_url})

            # Viết URL vào tệp urls.txt
            urls_file.write(category_url + article_url + "\n")
        
    print("Các URL đã được ghi vào tệp urlsdantri.txt.")

else:
    print("Lỗi: Không thể truy cập trang web")
