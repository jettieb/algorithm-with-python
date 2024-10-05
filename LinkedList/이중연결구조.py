class DNode:
    def __init__ (self, elem, prev=None, next=None):
        self.data = elem
        self.prev = prev    # 이전 노드를 위한 링크
        self.next = next    # 다음 노드를 위한 링크

    def append(self, node):
        if node is not None:
            node.next = self.next
            node.prev = self
            if self.next is not None:
                self.next.prev = node
            self.next = node

    # 다음 노드 꺼내기
    def popNext(self):
        node = self.next
        # 다음 노드가 빈 노드가 아니라면
        if node is not None:
            self.next = node.next
            if self.next is not None:
                self.next.prev = self
        return node

class DbLinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None
    
    def getNode(self, pos):
        if pos < 0 : return None
        ptr = self.head
        for i in range(pos):
            if ptr == None:
                return None
            ptr = ptr.next

    def getEntry(self, pos):
        node = self.getNode(pos)
        if node == None: return None
        else: return node.data

    # pos 위치에 새로운 요소 삽입
    def insert(self, pos, e):
        node = DNode(e) # 삽입할 새로운 노드
        before = self.getNode(pos - 1)
        # 이전 노드가 비어있는 경우 머리노드로 변경
        if before == None:
            node.next = self.head
            # 헤드노드가 비어있지 않았던 경우
            if node.next is not None:
                node.next.prev = node
            self.head = node    # 해드노드 변경
        else: before.append(node)

    # pos 위치의 요소 삭제
    def delete(self, pos):
        before = self.getNode(pos)
        # 머리노드 삭제
        if before == None:
            before = self.head
            # 헤드노드 있는 경우
            if self.head != None:
                self.head = self.head.next
            # 헤드노드가 없는 경우
            if self.head == None:
                self.head.prev = None
            return before
        else: before.popNext()

