import sys

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

def evaluate(operator, a, b, variables):
    def parse_int(value):
        try:
            return int(value)
        except ValueError:
            return 0
        
    if a in variables:
        a = int(variables[a])
    else:
        a = parse_int(a)

    if b in variables:
        b = int(variables[b])
    else:
        b = parse_int(b)

    if operator == 'ADD':
        return a + b
    elif operator == 'SUB':
        return a - b
    elif operator == 'MUL':
        return a * b
    elif operator == 'DIV':
        return a / b
    elif operator == '<':
        return a < b
    elif operator == '<=':
        return a <= b
    elif operator == '>':
        return a > b
    elif operator == '>=':
        return a >= b
    elif operator == '==':
        return a == b
    elif operator == '!=':
        return a != b
    else:
        return None


def execute_intermediate_code(code):
    stack = Stack()
    whileStack = Stack()
    variables = {}
    line = 0

    instructions = code.split('\n')
    while line < len(instructions):
        instruction = instructions[line]
        if instruction.startswith('PUSH'):
            _, value = instruction.split()
            if value != 'BLANK':
                stack.push(value)
        elif instruction.startswith('ASSIGN'): # ASSIGN variable value
            _, variable, value = instruction.split()
            variables[variable] = value if value != 'BLANK' else stack.peek() 
        elif instruction in ['ADD', 'SUB', 'MUL', 'DIV']:
            operand2 = stack.pop()
            operand1 = stack.pop()
            
            result = evaluate(instruction, operand1, operand2, variables)
            stack.push(result)
        elif instruction == 'PRINT':
            value = stack.pop()
            print(value)
        elif instruction.startswith('BEXPRESSION'): # BEXPRESSION operand1 operator operand2
            _, operand1, operator, operand2 = instruction.split()
            result = evaluate(operator, operand1 if operand1 != 'BLANK' else stack.peek(), operand2 if operand2 != 'BLANK' else stack.peek(), variables)
            stack.push(result)
        elif instruction == 'IF':
            condition = stack.pop()
            if condition:
                line += 1  # Skip block
            else:
                # Find the corresponding ELSE or ENDIF instruction
                endifCount = 0
                tmp = line + 1
                while tmp < len(instructions):
                    if instructions[tmp] == 'IF':
                        endifCount += 1
                    elif instructions[tmp] in ['ELSE', 'ENDIF']:
                        if endifCount == 0:
                            line = tmp + 1 # Jump to ENDIF block or ENDIF
                            break
                        else:
                            endifCount -= 1

                    tmp += 1
            
            continue
        elif instruction == 'ELSE': # It appears when the if condition is false
            endifCount = 0
            tmp = line + 1
            while tmp < len(instructions):
                if instructions[tmp] == 'IF':
                    endifCount += 1
                elif instructions[tmp] == 'ENDIF':
                    if endifCount == 0:
                        line = tmp + 1 # Jump to ENDIF block
                        break
                    else:
                        endifCount -= 1

                tmp += 1
            continue
        elif instruction == 'WHILE':
            whileStack.push(line)
            condition = stack.pop()
            if condition:
                line += 1  # Skip block
            else:
                # Find the corresponding 'ENDO' instruction
                endoCount = 0
                tmp = line + 1
                while tmp < len(instructions):
                    if instructions[tmp] == 'WHILE':
                        endoCount += 1
                    elif instructions[tmp] == 'ENDO':
                        if endoCount == 0:
                            line = tmp + 1 # Jump to ENDO block
                            break
                        else:
                            endoCount -= 1

                    tmp += 1
            continue
        elif instruction == 'ENDO':
            loopStart = whileStack.pop()  # Get the loop start position
            line = loopStart - 1  # Jump back to the start of the loop (BEXPRESSION)
            continue
        line += 1

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            contents = file.read()
        return contents
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except IOError:
        print(f"Error: Unable to read file '{filename}'.")


filename = sys.argv[1]
file = read_file(filename)
if file:
    execute_intermediate_code(file)
        
# intermediate_code = '''
# ASSIGN i 1
# ASSIGN n 10
# BEXPRESSION i <= n
# WHILE
# PUSH n
# PUSH 2
# DIV
# BEXPRESSION i < BLANK
# IF
# PUSH i
# PUSH 100
# ADD
# PUSH BLANK
# PRINT
# ELSE
# PUSH 100
# PUSH i
# SUB
# PUSH BLANK
# PRINT
# ENDIF
# PUSH i
# PUSH 1
# ADD
# ASSIGN i BLANK
# ENDO
# '''

# execute_intermediate_code(intermediate_code)
