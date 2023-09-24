import os

# Đường dẫn tới thư mục gốc của corpus
corpus_directory = r"D:\Master\Master-Code\CodePythonMaster\7 XuLiNNTuNhien\Bai1\Data\new test"

# Khởi tạo biến đếm số lượng sub-directories, số lượng document và thông tin thống kê
topic_data = {}
total_files = 0

# Duyệt qua các thư mục con trong thư mục gốc
for root, subdirs, files in os.walk(corpus_directory):
    for subdir in subdirs:
        topic = subdir  # Lấy tên thư mục con làm tên chủ đề
        topic_path = os.path.join(root, subdir)
        
        # Đếm số lượng tệp tin trong thư mục con và lấy kí tự đầu tiên đến ký tự gạch dưới (_) làm "Topic ID"
        topic_files = len([f for f in os.listdir(topic_path) if f.endswith(".txt")])

        topicID = [f for f in os.listdir(topic_path) if f.endswith(".txt")]
        topicID0 = topicID[0].split('_')[0]
        
        # Cập nhật thông tin chủ đề và đếm số lượng tệp
        topic_data[topic] = {"TopicID": topicID0, "#files": topic_files}
        total_files += topic_files

# In số liệu thống kê theo từng chủ đề
print("Topic\t\tTopic ID\t#files")
print("*" * 50)

for topic, data in topic_data.items():
    print(f"{topic}\t\t{data['TopicID']}\t\t{data['#files']}")

# Tính và in tổng số lượng document
print("\nTotal")
print(f"{'Total':<10}{total_files}")

# In số lượng các loại topic
print("\nSố lượng các loại topic:")
print(len(topic_data))
