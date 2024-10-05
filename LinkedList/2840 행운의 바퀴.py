def arrow(n,k):
    wheel = [None] * n
    idx = 0
    for i in range(k):
        # 입력받기
        num, alp = map(str, input().split())
        num = int(num)

        idx = (idx + num) % n   # 인덱스 번호
        # 만약 이미 차있는데 입력받은 알파벳과 동일하지 않다면 False 반환.
        if (wheel[idx] is not None) and (wheel[idx] != alp):
            print("!")
            return False
        wheel[idx] = alp

        # 이미 중복되는 알파벳이 있는 경우 False
        count = 0
        for l in range(n):
            if wheel[l] == alp:
                count += 1
        if count > 1:
            print("!")
            return False
    
    return wheel, idx

n, k = map(int, input().split())
result = arrow(n,k)

# 결과가 False가 아닌 경우만 출력
if result:
    wheel, idx = result
    for _ in range(n):
        if wheel[idx] is not None:
            print(wheel[idx], end="")
        else:
            print("?", end="")
        idx = (idx - 1) % n