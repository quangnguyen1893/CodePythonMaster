class Stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        else:
            raise Exception("Empty Stack")

    def getSize(self):
        return len(self.stack)

    def empty(self):
        self.stack = []


class MyProgram:
    def __init__(self):
        self.stack = Stack()
        self.listVariable = {}
        self.stackStatememt = Stack()
        self.numStatement = 0
        self.infoStatement = {}
        self.flagCondition = False
        self.flagCompare = False
        self.listCompare = ["T_LESSTHAN", "T_LESSTHAN_EQUAL", "T_GREATER", "T_GREATER_EQUAL", "T_EQUAL", "T_NOT_EQUAL"]
        self.skipIf = False
        self.skipElse = False
        self.startSkip = False
        self.skipWhile = False
        self.startWhile = False
        self.listStatementWhile = []
        self.conditionWhile = Stack()

    def getSizeStack(self):
        return self.stack.getSize()

    def pushNewStatement(self, stm):
        self.stackStatememt.push(self.numStatement)
        self.infoStatement[self.numStatement] = {}
        self.infoStatement[self.numStatement]['firstOp'] = []
        self.infoStatement[self.numStatement]['lastOp'] = []
        self.infoStatement[self.numStatement]['type'] = stm;
        self.numStatement += 1
        self.flagCondition = True

    def readNewItem(self, item):
        if self.startWhile:
            self.listStatementWhile.append(item)
        val = item.strip().split()
        # print("Item: "+item)
        # print(self.listVariable)
        if self.skipWhile:
            if val[0] == "ENDO":
                self.skipWhile = False
        elif self.skipIf:
            if val[0] == "ELSE" or val[0] == "ENDIF":
                self.skipIf = False
            # if (val[0] == "ELSE"):
            #     print("else")
            #     #thuc thi doan else
            # continue with another line
        elif self.skipElse and self.startSkip:
            # print("Skip")
            if val[0] == "ENDIF":
                self.skipElse = False
                self.startSkip = False
        elif (self.flagCondition and self.flagCompare):
            # print("toan tu thu 2")
            # print(2)
            # self.infoStatement[self.numStatement - 1]['lastOp']
            tmp = ''
            if val[0] == 'PUSH':
                tmp = 'PUSH '+val[1]
            elif val[0] == 'VARIABLE':
                tmp = "VARIABLE " + val[1]
            elif val[0] in ["ADD", "SUB", "MUL", "DIV"]:
                tmp = val[0]
            elif val[0] == 'DO' or val[0] == 'THEN':
                self.flagCondition = False
                self.flagCompare = False
                # resCheck = self.checkCondition(self.infoStatement[self.numStatement - 1])
                # print(resCheck)
                if (self.checkCondition(self.infoStatement[self.numStatement - 1])):
                    # condition TRUE
                    if self.infoStatement[self.numStatement - 1]['type'] == "IF":
                        # -> skip else
                        self.skipElse = True
                        self.skipIf = False
                    else:
                        self.skipWhile = False
                        self.startWhile = True
                        self.conditionWhile.push(self.infoStatement[self.numStatement - 1])
                else:
                    # condition FASLE
                    if self.infoStatement[self.numStatement - 1]['type'] == "IF":
                        # -> go to else
                        self.skipIf = True
                        self.skipElse = False
                    else:
                        self.skipWhile = True
                        self.startWhile = False

            # tmp = "not appear"
            if (tmp != ''):
                self.infoStatement[self.numStatement - 1]['lastOp'].append(tmp)
        elif (self.flagCondition):
            # print("toan tu dau tien")
            # print(1)
            tmp = ''
            if val[0] == 'PUSH':
                tmp = 'PUSH '+val[1]
            elif val[0] == 'VARIABLE':
                tmp = "VARIABLE " + val[1]
            elif val[0] in ["ADD", "SUB", "MUL", "DIV"]:
                tmp = val[0]
            elif val[0] in self.listCompare:
                self.infoStatement[self.numStatement - 1]['comp'] = val[0]
                self.flagCompare = True
                # print("comparing")
            if (tmp != ''):
                self.infoStatement[self.numStatement - 1]['firstOp'].append(tmp)
        elif val[0] == 'PUSH':
            self.stack.push(val[1])
        elif val[0] == 'TO':
            # print(val)
            # print(self.getSizeStack())
            self.listVariable[val[1]] = int(self.stack.pop())
            # listVariable[val[1]] = int(self.pop())
            # print(f"Lis variable : {self.listVariable}")
        elif val[0] == 'PRINT':
            self.printCmd()
        elif val[0] == 'WHILE' or val[0] == 'IF':
            self.pushNewStatement(val[0])
        elif val[0] == 'ELSE' and self.skipElse:
            self.startSkip = True
        elif val[0] == 'VARIABLE':
            self.stack.push(self.listVariable[val[1]])
        elif val[0] == 'ENDO':
            # print(self.listStatementWhile)
            # print(self.listVariable)
            listStatement = self.listStatementWhile
            self.listStatementWhile = []
            reCheckCondition = self.conditionWhile.pop()
            if (self.checkCondition(reCheckCondition)):
                #true, continue while, reset
                self.skipWhile = False
                self.startWhile = True
                # print("ok -> true, loop")
                self.conditionWhile.push(reCheckCondition)
                for itemLoop in listStatement:
                    self.readNewItem(itemLoop)
                # return listStatement
            else:
                #flase, end while
                self.skipWhile = False
                self.startWhile = False

        elif val[0] == 'ADD':
            num1 = self.stack.pop()
            num2 = self.stack.pop()
            self.stack.push(int(num2) + int(num1))
        elif val[0] == 'SUB':
            num1 = self.stack.pop()
            num2 = self.stack.pop()
            self.stack.push(int(num2) - int(num1))
        elif val[0] == 'MUL':
            num1 = self.stack.pop()
            num2 = self.stack.pop()
            self.stack.push(int(num2) * int(num1))
        elif val[0] == 'DIV':
            num1 = self.stack.pop()
            num2 = self.stack.pop()
            self.stack.push(int(num2) / int(num1))
        # return ''

    def printCmd(self):
        #print(">>>>>> PRINT >>>>>> ", end="")
        print(self.stack.pop())

    def printTest(self):
        print("Print test: ")
        print(self.stack)
        print(self.getSizeStack())
        print(self.listVariable)
        print(self.infoStatement)

    def checkCondition(self, condition):
        # print("condition >>> ")
        firstOp = self.readOperator(condition['firstOp'])
        lastOp = self.readOperator(condition['lastOp'])
        # print(firstOp)
        # print(condition['comp'])
        # print(lastOp)
        # print(condition['type'])
        if condition['comp'] == "T_LESSTHAN":
            return int(firstOp) < int(lastOp)
        elif condition['comp'] == "T_LESSTHAN_EQUAL":
            return int(firstOp) <= int(lastOp)
        elif condition['comp'] == "T_GREATER":
            return int(firstOp) > int(lastOp)
        elif condition['comp'] == "T_GREATER_EQUAL":
            return int(firstOp) >= int(lastOp)
        elif condition['comp'] == "T_EQUAL":
            return int(firstOp) == int(lastOp)
        elif condition['comp'] == "T_NOT_EQUAL":
            return int(firstOp) != int(lastOp)


    def readOperator(self, operator):
        tmpS = Stack()
        # print(operator)
        for i in operator:
            ival = i.strip().split()
            # print(ival)
            if ival[0] == "VARIABLE":
                tmpS.push(self.listVariable[ival[1]])
            elif ival[0] == "PUSH":
                tmpS.push(ival[1])
            elif ival[0] == "ADD":
                num1 = tmpS.pop()
                num2 = tmpS.pop()
                tmpS.push(int(num2) + int(num1))
            elif ival[0] == "SUB":
                num1 = tmpS.pop()
                num2 = tmpS.pop()
                tmpS.push(int(num2) - int(num1))
            elif ival[0] == "MUL":
                num1 = tmpS.pop()
                num2 = tmpS.pop()
                tmpS.push(int(num2) * int(num1))
            elif ival[0] == "DIV":
                num1 = tmpS.pop()
                num2 = tmpS.pop()
                tmpS.push(int(num2) / int(num1))
        return tmpS.pop()


myPro = MyProgram()
listVariable = {}
condition = Stack()
flagCondition = False


with open('/home/quang/CodePythonMaster/5 LyThuyetThongTin/Baitaplon/Bai2/Bai2.2/result3.txt', 'r') as f:
    for line in f:
        res = myPro.readNewItem(line)


# from commandline
# import sys
# input = sys.argv[1]
# with open(input, 'r') as f:
#     for line in f:
#         res = myPro.readNewItem(line)