n = int(input())
k = int(input())
sensor = list(map(int, input().split()))   # 집중국
sensor.sort()

between = list()    # 집중국 들의 사이 거리
for i in range(n-1):
    between.append(sensor[i + 1] - sensor[i])
between.sort()

# 센서때문에 제외되는 사이 거리 고려하여 슬라이싱
print(sum(between[:n-k]))