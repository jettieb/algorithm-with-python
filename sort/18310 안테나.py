n = int(input())
house = list(map(int, input().split()))
house.sort()

"""
total = {}  # 모든 집까지 거리의 합. (key: 집 위치, value: 다른 집들과의 총 거리)

for h in house:
    total[h] = 0
    for j in house:
        # 모든 집 사이의 거리 합
        total[h] += abs(h - j)

sort_short = sorted(total.items(), key = lambda x: x[1])

# 이렇게 dictionary로 각 집 별로 총 이동 거리 총합을 구했으나, 시간초과가 뜸.
"""
print(house[(n - 1)//2])