# 원형 큐를 상속받아 원형 덱 구현

# 원형 큐
class ArrayQueue:
    def __init__(self, capacity = 10):
        self.capacity = capacity
        self.array = [None]*capacity
        self.front = 0
        self.rear = 0

    def isEmpty(self):
        return self.front == self.rear
    
    def isFull(self):
        return self.front == (self.rear + 1) % self.capacity
    
    def enqueue(self, item):
        if not self.isFull():
            self.rear = (self.rear + 1) % self.capacity
            self.array[self.rear] = item
        else: pass

    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front + 1) % self. capacity
            return self.array[self.front]
        else: pass

    def peek(self):
        if not self.isEmpty():
            return self.array[(self.front + 1) % self.capacity]
        else: pass

    def size(self):
        return (self.rear - self.front + self.capacity) % self.capacity
    
    def display(self, message=""):
        print(message, self.array)
    

# 원형 덱
class CircularDeque(ArrayQueue):
    def __init__(self, capacity = 10):
        super().__init__(capacity)
        # 덱에서 추가되는 데이터는 없고, 부모 클래스의 데이터만 초기화.

    # 동작이 동일하지만, 이름만 변경되는 연산
    def addRear(self, item): self.enqueue(item)
    def deleteFront(self): return self.dequeue()
    def getFront(self): return self.peek()

    def addFront(self, item):
        if not self.isFull():
            self.array[self.front] = item
            self.front = (self.front - 1 + self.capacity) % self.capacity
            # 음수일 경우 대비
        else: pass
    
    def deleteRear(self):
        if not self.isEmpty():
            item = self.array[self.rear]
            self.rear = (self.rear - 1 + self.capacity) % self.capacity
            return item
        else: pass

    def getRear(self):
        if not self.isEmpty():
            return self.array[self.rear]
        else: pass


# 활용
dq = CircularDeque()

for i in range(9):
    if i%2==0 : dq.addRear(i)
    else: dq.addFront(i)
dq.display("홀수는 전단 짝수는 후단 삽입")

for i in range(2):dq.deleteFront()
for i in range(3):dq.deleteRear()
dq.display("전단 삭제 2번, 후단 삭제 3번")

for i in range(9, 14): dq.addFront(i)
dq.display("전단에 9~13 삽입")
