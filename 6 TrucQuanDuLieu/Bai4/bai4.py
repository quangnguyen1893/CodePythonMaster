import xml.etree.ElementTree as ET

# Đường dẫn đến tệp XML
xml_file_path = "D:/Master/Master-Code/CodePythonMaster/6 TrucQuanDuLieu/Bai4/spam.xml"

# Phân tích cây XML từ tệp
tree = ET.parse(xml_file_path)
root = tree.getroot()

# Hàm đệ quy để đếm số nút lá
def count_leaf_nodes(node):
    if len(node) == 0:
        return 1
    count = 0
    for child in node:
        count += count_leaf_nodes(child)
    return count

# Đếm số nút lá trong cây XML
leaf_node_count = count_leaf_nodes(root)

print("Số nút lá trong cây XML là:", leaf_node_count)
