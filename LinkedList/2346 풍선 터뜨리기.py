# 풍선이 원형으로 존재
# -N 부터 N 까지의 임의로 들어있는 숫자만큼 이동해서 풍선 터뜨리기

n = int(input()) # 풍선 갯수
num = list(map(int, input().split()))   # 풍선에 들어있을 종이의 숫자
index = list(range(1, n+1)) # 몇 번째 풍선이 터졌는지 확인하기 위함.

result = []
idx = 0

for i in range(n):
    result.append(index[idx])
    if len(num) - 1 != 0:
        index.pop(idx)
        move = num.pop(idx)
        if move > 0:
            idx = (idx + move - 1) % (len(num))
        else:
            idx = (idx + move) % (len(num))

for r in result:
    print(r, end=" ")