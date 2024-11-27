import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())    # 가로, 세로
box = []  # 토마토 상자
for _ in range(n): 
    box.append(list(map(int, input().split())))
day = 0

# 익은 토마토(1)의 좌표 큐에 저장
q = deque()
for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            q.append([i, j])

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
while q:
    x, y = q.popleft()
    for i in range(4):
        # 익은 토마토 상하좌우 돌면서 익은 날짜 저장
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if box[nx][ny] == 0:
                box[nx][ny] = box[x][y] + 1
                q.append([nx, ny])

ans = 0
for line in box:
    for tomato in line:
        if tomato == 0:
            # 토마토가 모두 익지 못한 상황
            print(-1)
            exit()
    ans = max(ans, max(line))   # 가장 최대 일자 찾기

print(ans-1)    # 1에서 시작했기 때문에 결과 값에서 1빼주기