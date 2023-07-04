class StackMachine:
    def __init__(self):
        self.stack = []
        self.variables = {}

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            raise ValueError("Stack is empty")

    def add(self):
        if len(self.stack) >= 2:
            b = self.stack.pop()
            a = self.stack.pop()
            result = a + b
            self.stack.append(result)
        else:
            raise ValueError("Không đủ toán hạng để thực hiện phép toán Cộng")

    def sub(self):
        if len(self.stack) >= 2:
            b = self.stack.pop()
            a = self.stack.pop()
            result = a - b
            self.stack.append(result)
        else:
            raise ValueError("Không đủ toán hạng để thực hiện phép toán Trừ")

    def mul(self):
        if len(self.stack) >= 2:
            b = self.stack.pop()
            a = self.stack.pop()
            result = a * b
            self.stack.append(result)
        else:
            raise ValueError("Không đủ toán hạng để thực hiện phép toán Nhân")

    def div(self):
        if len(self.stack) >= 2:
            b = self.stack.pop()
            a = self.stack.pop()
            result = a / b
            self.stack.append(result)
        else:
            raise ValueError("Không đủ toán hạng để thực hiện phép toán Chia")

    def variable(self, name):
        if name in self.variables:
            value = self.variables[name]
            self.push(value)
        else:
            raise ValueError(f"Biến chưa đc định nghĩa: {name}")

    def execute(self, instructions):
        for instruction in instructions:
            parts = instruction.split()

            if parts[0] == "PUSH":
                value = int(parts[1])
                self.push(value)
            elif parts[0] == "TO":
                variable = parts[1]
                value = self.pop()
                self.variables[variable] = value
            elif parts[0] == "VARIABLE":
                variable = parts[1]
                self.variable(variable)
            elif parts[0] == "ADD":
                self.add()
            elif parts[0] == "SUB":
                self.sub()
            elif parts[0] == "MUL":
                self.mul()
            elif parts[0] == "DIV":
                self.div()
            elif parts[0] == "PRINT":
                print(self.stack[-1])
            else:
                raise ValueError("Không hợp lệ")

stack_machine = StackMachine()

def docfile(path):
    with open(path, 'r') as file:
        rs = file.read().splitlines()
    return rs
# Chuỗi lệnh
path = '/home/quang/CodePythonMaster/5 LyThuyetThongTin/Baitaplon/Bai2/Bai2.1/result2.txt'
string_command = docfile(path)
try:
    instructions = string_command
    stack_machine.execute(instructions)
except Exception as e:
    print(e)
