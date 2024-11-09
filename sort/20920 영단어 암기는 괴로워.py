### 처음에 2차원 배열로 풀었으나, 시간초과가 떠서 dictionary로 변경
### 변경해도 계속 시간초과가 떠서, input() 으로 받지 않고 sys.stdin.read 사용해서 입력받음
import sys

n,m = map(int, input().split())
word = {}   # 딕셔너리로 만들기(key: 단어, value: 횟수)

# word 배열에 넣기
for _ in range(n):
    # strip은 문자열 맨 앞과 맨 끝의 공백문자 제거
    w = sys.stdin.readline().strip()

    # m보다 짧은 길이는 pass
    if len(w) < m:
        continue

    # 이미 배열에 존재하는지 확인
    if w in word:
        word[w] += 1
    else:
        word[w] = 1

""" 
sort_word = sorted(word.items(), key=lambda x: (-x[1],-len(x[0]),x[0]))
이렇게 정렬 한번에 작성해도됨.
"""

# dictionary 한번 정렬하면 list로 변경됨!
# 3. 알파벳 사전 순으로 앞에 있는 단어일수록 앞에 배치한다
sort_alp = sorted(word.items(), key=lambda x: x[0])
# 2. 해당 단어의 길이가 길수록 앞에 배치한다.
sort_length = sorted(sort_alp, key=lambda x: len(x[0]), reverse=True)
# 1. 자주 나오는 단어일수록 앞에 배치한다.
sort_frequency = sorted(sort_length, key=lambda x: x[1], reverse=True)

for item in sort_frequency:
    print(item[0])