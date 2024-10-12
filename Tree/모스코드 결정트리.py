class BTNode:
    def __init__(self, elem, left=None, right=None):
        self.data = elem
        self.left = left
        self.right = right

table = [('A', '.-'), ('B', '-...'),
         ('C', '-.-.'), ('D', '-..'), ('E', '.'),
         ('F', '..-.'), ('G', '--.'), ('H', '....'),
         ('I', '..'), ('J', '.---'), ('K', '-.-'),
         ('L', '.-..'), ('M', '--'), ('N', '-.'),
         ('O', '---'), ('P', '.--.'), ('Q', '--.-'),
         ('R', '.-.'), ('S', '...'), ('T', '-'),
         ('U', '..-'), ('V', '...-'), ('W', '.--'),
         ('X', '-..-'), ('Y', '-.--'), ('Z', '--..')]

def encode(ch):
    idx = ord(ch)-ord('A')  # ord()는 문자를 아스키 코드값으로 바꿔줌.
    return table[idx][1]

def make_morse_tree():
    root = BTNode(None, None, None)
    for tp in table:
        code = tp[1]
        node = root
        for c in code:
            if c == '.':
                if node.left == None:
                    node.left = BTNode(None, None, None)
                node = node.left
            elif c == '-':
                if node.right == None:
                    node.right = BTNode(None, None, None)
                node = node.right
        
        # 최종 노드에 문자 부여
        node.data = tp[0]
    return root

def decode(root, code):
    node = root
    for c  in code:
        if c == '.' :
            node = node.left
        elif c == '-':
            node = node.right
    return node.data


morseCodeTree = make_morse_tree()
str = input("입력문장: ")
mlist = []
for ch in str:
    mlist.append(encode(ch))
print("Morse Code:", mlist)
print("Decoding:", end='')
for code in mlist:
    ch = decode(morseCodeTree, code)
    print(ch, end='')