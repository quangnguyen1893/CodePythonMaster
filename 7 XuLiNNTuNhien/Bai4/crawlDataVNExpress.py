import os
import requests
from bs4 import BeautifulSoup
import shutil

# Địa chỉ URL của trang web báo và chuyên mục bạn muốn crawl
base_url = "https://vnexpress.net"  # Thay bằng URL thực tế
category_url = base_url + "/giao-duc"  # Thay bằng URL chuyên mục thực tế

# Tạo thư mục 'giaoducvnexpress' nếu nó chưa tồn tại
if not os.path.exists("/home/quang/CodePythonMaster/7 XuLiNNTuNhien/Bai4/giaoducvnexpress"):
    os.makedirs("/home/quang/CodePythonMaster/7 XuLiNNTuNhien/Bai4/giaoducvnexpress")

# Gửi yêu cầu HTTP để lấy trang web
response = requests.get(category_url)

# Kiểm tra xem yêu cầu có thành công không
if response.status_code == 200:
    # Sử dụng BeautifulSoup để phân tích HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # Tìm tất cả các thẻ liên quan đến bài báo, ví dụ như thẻ h3 với class "title-news"
    article_links = soup.find_all("h3", class_="title-news")  # Thay class bằng class thực tế

    # Lưu trữ thông tin về tiêu đề và URL của các bài báo
    articles_info = []

    # In ra các tiêu đề và URL của 50 bài đầu tiên
    for link in article_links[:50]:
        article_url = link.a['href']
        article_title = link.a.text
        articles_info.append({"Tiêu đề": article_title, "URL": article_url})

    # Lặp qua danh sách bài báo và lưu nội dung vào các tệp tin .txt riêng biệt
    for i, article in enumerate(articles_info, start=1):
        article_url = article["URL"]
        article_title = article["Tiêu đề"]

        article_response = requests.get(article_url)
        if article_response.status_code == 200:
            article_soup = BeautifulSoup(article_response.text, "html.parser")
            article_descript = article_soup.find("p", class_="description").get_text() 
            article_content = article_soup.find("article", class_="fck_detail").get_text()  # Thay thẻ và class bằng thực tế
            filename = f"/home/quang/CodePythonMaster/7 XuLiNNTuNhien/Bai4/giaoducvnexpress/article_{i}.txt"
            file_path = os.path.join("/home/quang/CodePythonMaster/7 XuLiNNTuNhien/Bai4/giaoducvnexpress", f"article_{i}.txt")

            # Tạo hoặc mở tệp tin .txt trong thư mục 'giaoducvnexpress' và ghi nội dung vào đó
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(f"{article_title}\n")
                file.write(f"{article_descript}\n")
                file.write(f"{article_content}")

            print(f"Bài {i} đã được lưu vào tệp {file_path}")

        else:
            print(f"Lỗi: Không thể truy cập nội dung bài {i}.")

else:
    print("Lỗi: Không thể truy cập trang web")
