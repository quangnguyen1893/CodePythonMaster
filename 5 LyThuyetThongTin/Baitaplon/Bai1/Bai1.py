class Stack: # khởi tạo 1 đối tượng stack và các hàm
    def __init__(self):
        self.items = []

    def push(self, item): #Thêm một phần tử vào đỉnh của ngăn xếp
        self.items.append(item)

    def pop(self): #Thêm một phần tử vào đỉnh của ngăn xếp
        if not self.is_empty():
            return self.items.pop()
        else:
            raise Exception("Stack rỗng")

    def is_empty(self): #Kiểm tra xem ngăn xếp có rỗng không
        return len(self.items) == 0


class SimpleVM: #Tạo 1 máy ảo
    def __init__(self):
        self.stack = Stack()# Tạo một đối tượng Stack mới để sử dụng trong máy ảo
        self.instructions = [] # Lưu trữ các lệnh thực thi của máy ảo
        self.output = [] # Lưu trữ kết quả đầu ra sau khi thực thi lệnh

    def load_command(self, program): #Nhận một danh sách các lệnh (program) làm đầu vào và lưu trữ nó vào biến instructions.
        self.instructions = program

    def execute(self): #Thực thi từng lệnh trong danh sách instructions. Dựa vào loại lệnh, nó gọi các phương thức tương ứng để thực hiện các phép toán và in kết quả.
        for instruction in self.instructions:
            if instruction == "PRINT":
                self.print()
            elif instruction.startswith("PUSH"):
                value = int(instruction.split()[1])
                self.push_value(value)
            elif instruction == "ADD":
                self.add()
            elif instruction == "SUB":
                self.subtract()
            elif instruction == "MUL":
                self.multiply()
            elif instruction == "DIV":
                self.divide()
            else:
                raise Exception(f"Không hợp lệ: {instruction}")

    def push_value(self, value): #Thêm một giá trị (value) vào đỉnh ngăn xếp (stack).
        self.stack.push(value)

    def print(self): #Lấy giá trị ở đỉnh ngăn xếp và lưu trữ nó vào danh sách output.
        top = self.stack.pop()
        self.output.append(top)

    def add(self): #Lấy hai giá trị từ đỉnh ngăn xếp, thực hiện phép cộng và đẩy kết quả vào đỉnh ngăn xếp.
        num2 = self.stack.pop()
        num1 = self.stack.pop()
        result = num1 + num2
        self.stack.push(result)

    def subtract(self): #Lấy hai giá trị từ đỉnh ngăn xếp, thực hiện phép trừ và đẩy kết quả vào đỉnh ngăn xếp.
        num2 = self.stack.pop()
        num1 = self.stack.pop()
        result = num1 - num2
        self.stack.push(result)

    def multiply(self): #Lấy hai giá trị từ đỉnh ngăn xếp, thực hiện phép nhân và đẩy kết quả vào đỉnh ngăn xếp.
        num2 = self.stack.pop()
        num1 = self.stack.pop()
        result = num1 * num2
        self.stack.push(result)

    def divide(self): #Lấy hai giá trị từ đỉnh ngăn xếp, thực hiện phép chia và đẩy kết quả vào đỉnh ngăn xếp. Nếu số chia là 0, nó sẽ ném một ngoại lệ (Exception) với thông báo "Lỗi chia cho 0".
        num2 = self.stack.pop()
        num1 = self.stack.pop()
        if num2 == 0:
            raise Exception("Lỗi chia cho 0")
        result = int(num1 / num2)
        self.stack.push(result)

    def get_output(self): #Trả về danh sách output chứa kết quả sau khi thực thi lệnh.
        return self.output

def docfile(path): #Đọc nội dung của tệp văn bản tại đường dẫn path và trả về một danh sách các dòng trong tệp.
    with open(path, 'r') as file:
        rs = file.read().splitlines()
    return rs

# Chuỗi lệnh thực thi
path = '/home/quang/CodePythonMaster/5 LyThuyetThongTin/Baitaplon/Bai1/result.txt'
string_command = docfile(path)

try:
    vm = SimpleVM()
    vm.load_command(string_command)
    vm.execute()

    output = vm.get_output()
    for value in output:
        print(value)
except Exception as e:
    print(e)