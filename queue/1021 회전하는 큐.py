# 앞 뒤로 값을 넣기 유용한 덱 사용
import collections

n, m = map(int, input().split())
index = map(int, input().split())
dq = collections.deque(range(1,n+1))    # 1부터 n까지 값 삽입
count = 0

for i in index:
    while True:
        # 1번
        if i == dq[0]:
            dq.popleft()
            break
        # 2번 - 앞의 것을 뒤로 뺴기
        # dq.index(e) 하면 e원소의 위치 알려줌.
        elif dq.index(i) < len(dq)/2:
            dq.append(dq.popleft())
            count += 1
        # 3번 - 맨 뒤의 것 앞으로 옮기기
        else:
            dq.appendleft(dq.pop())
            count += 1

print(count)