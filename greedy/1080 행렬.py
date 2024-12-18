from sys import stdin
                
N,M = map(int,stdin.readline().split())
A = [list(map(int,stdin.readline().rstrip())) for _ in range(N)]
B = [list(map(int,stdin.readline().rstrip())) for _ in range(N)]

# 3x3 뒤집기 함수
def toggle(r,c):
    for i in range(r,r+3):
        for j in range(c,c+3):
            A[i][j] = 1 - A[i][j]

cnt = 0
for i in range(N-2):
    for j in range(M-2):
        # 맨 오른쪽이 같지 않으면 행렬 뒤집기
        if A[i][j] != B[i][j]:
            toggle(i,j)
            cnt += 1

print(cnt if A == B else -1)