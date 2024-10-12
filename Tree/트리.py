import queue

class BTNode:
    def __init__(self, elem, left=None, right=None):
        self.data = elem
        self.left = left
        self.right = right

# 전위순회 (VLR)
def preorder(n):
    if n is not None:
        print(n.data, end='')
        preorder(n.left)
        preorder(n.right)

# 중위순회 (LVR)
def inorder(n):
    if n is not None:
        inorder(n.left)
        print(n.data, end='')
        inorder(n.right)

# 후위순회(LRV)
def postorder(n):
    if n is not None:
        postorder(n.left)
        postorder(n.right)
        print(n.data, end='')

# 레벨순회
def levelorder(root):
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        n = q.get()
        if n is not None:
            print(n.data, end='')
            q.put(n.left)
            q.put(n.right)

# 전체 노드의 수 구하기
def count_node(n):
    if n is None:
        return 0
    else:
        return count_node(n.left) + count_node(n.right) + 1

# 트리 높이 구하기
def calc_height(n):
    if n is None:
        return 0
    hLeft = calc_height(n.left)
    hRight = calc_height(n.right)
    # 큰 값에 1 더해서 반환
    if(hLeft > hRight):
        return hLeft + 1
    else: return hRight + 1