import os
from underthesea import sent_tokenize, word_tokenize

# Đường dẫn đến tệp tin trong corpus
corpus_directory = r"D:\Master\Master-Code\CodePythonMaster\7 XuLiNNTuNhien\Bai1\Data\new test"

# Khởi tạo biến đếm số lượng câu và số lượng từ
num_sentences = 0
num_words = 0
max_sentence_length = 0
min_sentence_length = float('inf')

# Duyệt qua các tệp tin trong corpus
for root, dirs, files in os.walk(corpus_directory):
    for file in files:
        if file.endswith(".txt"):
            file_path = os.path.join(root, file)
            
            # Đọc nội dung tệp tin
            with open(file_path, "r", encoding="latin-1") as f:
                text = f.read()
            
            # Tách câu và từ
            sentences = sent_tokenize(text)
            words = word_tokenize(text)

            # Cập nhật biến đếm
            num_sentences += len(sentences)
            num_words += len(words)

            # Cập nhật độ dài câu ngắn nhất và dài nhất
            for sentence in sentences:
                sentence_length = len(word_tokenize(sentence))
                if sentence_length > max_sentence_length:
                    max_sentence_length = sentence_length
                if sentence_length < min_sentence_length:
                    min_sentence_length = sentence_length

# Tính độ dài trung bình của câu
average_sentence_length = num_words / num_sentences

# In số liệu thống kê
print(f"Số lượng câu: {num_sentences}")
print(f"Số lượng từ: {num_words}")
print(f"Câu dài nhất có {max_sentence_length} từ")
print(f"Câu ngắn nhất có {min_sentence_length} từ")
print(f"Độ dài trung bình của câu: {average_sentence_length:.2f} từ")
