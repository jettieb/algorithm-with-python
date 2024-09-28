class ArrayStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.array = [None]*capacity
        self.top = -1

    def isEmpty(self): return self.top == -1
    def isFull(self): return self.top == self.capacity -1

    def push(self, item):
        if not self.isFull():
            self.top += 1
            self.array[self.top] = item
        else: pass  #overflow 예외 처리하지 않음.

    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.array[self.top + 1]
        else: pass
        
    def peek(self):
        if not self.isEmpty():
            return self.array[self.top]
        else: pass

    def size(self): return self.top + 1


def checkBrackets(statement):
    stack = ArrayStack(100)
    for ch in statement:
        # 열리는 괄호면 stack에 삽입
        if ch in ('{', '(', '['):
            stack.push(ch)
        # 닫히는 괄호인 경우
        elif ch in ('}', ')', ']'):
            # 스택이 비어있으면 실패
            if stack.isEmpty():
                return False
            else:
                left = stack.pop()
                if (ch == '}' and left != '{') or \
                (ch == ')' and left != '(') or \
                (ch == ']' and left != '['):
                    return False
                
    return stack.isEmpty()  # 스택이 공백이면 True, 아니면 False

ment = "{a[(i+1)]=0;}"
print(checkBrackets(ment))