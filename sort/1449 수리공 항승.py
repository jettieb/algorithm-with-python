n,l = map(int, input().split())
water = list(map(int, input().split())) #  물 새는 곳 리스트
water.sort()
cnt = 1 # 총 테이프 개수
location = water[0] - 0.5 # 테이프 처음 붙이는 위치

for i in water[1:]:
    # 이미 붙어있는 테이프로 막아지지 않는 경우
    if i > location + l:
        cnt += 1
        location = i - 0.5

print(cnt)