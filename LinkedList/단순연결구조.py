class Node:
    def __init__(self, elem, link=None):
        self.data = elem
        self.link = link

    # self 다음에 node 넣기
    def append(self, node):
        if node is not None:
            node.link = self.link
            self.link = node
    
    # 현재 노드의 바로 뒤 노드 꺼내기
    def popNext(self):
        next = self.link
        if next is not None:
            self.link = next.link
        return next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def isEmpty(self):
        self.head == None

    def getNode(self, pos):
        if pos < 0 : return None
        ptr = self.head #시작위치
        for i in range(pos):
            if ptr == None:
                return None
            ptr = ptr.link
    
    def getEntry(self, pos):
        node = self.getNode(pos)
        if node == None : return None
        else: return node.data

    def insert(self, pos, e):
        # 새로운 노드
        node = Node(e, None)
        # 이전 노드 찾기
        before = self.getNode(pos - 1)
        # 이전 노드가 맨 앞이어서 헤드링크 변경해야하는 경우
        if before == None:
            node.link = self.head
            self.head = node
        else: before.append(node)

    def delete(self, pos):
        before = self.getNode(pos - 1)
        # before 노드가 맨 앞인 경우 헤드링크 변경
        if before == None:
            before = self.head
            if self.head is not None:
                self.head = self.head.list
            return before
        else: return before.popNext()

    def size(self):
        ptr = self.head
        count = 0
        while ptr is not None:
            ptr = ptr.link
            count += 1
        return count
