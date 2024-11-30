n = int(input())
meet = []
for _ in range(n):
    meet.append(list(map(int, input().split())))
ans = 0 # 정답 회의 수
end = 0 # 회의 종료 시간

meet.sort(key=lambda x: (x[1], x[0]))   # 종료 순으로 먼저 정렬

for s, e in meet:   
    if s >= end:
        ans += 1
        end = e

print(ans)