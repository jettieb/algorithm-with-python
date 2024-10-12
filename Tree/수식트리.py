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

def evaluate(node):
    if node is None:
        return 0
    # 단말노드인 경우
    elif (node.left and node.right) is None:
        return node.data
    else:
        op1 = evaluate(node.left)
        op2 = evaluate(node.right)
        if node.data == '+': return op1 + op2
        elif node.data == '-': return op1 - op2
        elif node.data == '*': return op1 * op2
        elif node.data == '/': return op1 / op2

# 후위표기 수식을 이용한 수식 트리 만들기
def buildETree(expr):
    if len(expr) == 0:
        return None

    token = expr.pop()
    # 연산자면 노드를 만들고, 오른쪽과 왼쪽 순으로 서브트리를 순환호출.
    if token in "+-*/":
        node = BTNode(token)
        node.right = buildETree(expr)
        node.left = buildETree(expr)
        return node
    # 피연산자면 단말노드이므로 노드를 만들어 바로 반환
    else:
        return BTNode(float(token))
    

str = input("입력(후위표기): ")
expr = str.split()
print("토큰분리: ", expr)
root = buildETree(expr)
print("계산결과:", evaluate(root))