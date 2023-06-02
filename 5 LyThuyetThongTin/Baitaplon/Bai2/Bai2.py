class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise Exception("Stack rỗng")

    def is_empty(self):
        return len(self.items) == 0


class SimpleVM:
    def __init__(self):
        self.stack = Stack()
        self.instructions = []
        self.output = []

    def load_command(self, program):
        self.instructions = program

    def execute(self):
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

    def push_value(self, value):
        self.stack.push(value)

    def print(self):
        top = self.stack.pop()
        self.output.append(top)

    def add(self):
        num2 = self.stack.pop()
        num1 = self.stack.pop()
        result = num1 + num2
        self.stack.push(result)

    def subtract(self):
        num2 = self.stack.pop()
        num1 = self.stack.pop()
        result = num1 - num2
        self.stack.push(result)

    def multiply(self):
        num2 = self.stack.pop()
        num1 = self.stack.pop()
        result = num1 * num2
        self.stack.push(result)

    def divide(self):
        num2 = self.stack.pop()
        num1 = self.stack.pop()
        if num2 == 0:
            raise Exception("Lỗi chia cho 0")
        result = int(num1 / num2)
        self.stack.push(result)

    def get_output(self):
        return self.output

def docfile(path):
    with open(path, 'r') as file:
        rs = file.read().splitlines()
    return rs

# Chuỗi lệnh
path = '/home/lighter/Documents/Master/CodeMaster/CodePythonMaster/5 LyThuyetThongTin/Baitaplon/Bai1/result.txt'
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