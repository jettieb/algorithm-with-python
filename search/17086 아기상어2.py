import sys
n,m = map(int, input().split())
sharks = []

# 상어 위치 추가
for i in range(n):
    # 한 행씩 받아오기 
    places = list(map(int, input().split()))
    for j, place in enumerate(places):
        if place == 1:
            # 상어의 위치 
            sharks.append((i, j))

res = 0
for i in range(n):
    for j in range(m):
        minDist = 1e9
        # 모든 상어와의 거리 구하기
        for x, y in sharks:
            distance = max(abs(i-x), abs(j-y))
            minDist = min(distance, minDist)
        # 모든 상어와의 최소 거리 중 최대 거리 구하기(최대 안전거리)
        res = max(minDist, res)

print(res)