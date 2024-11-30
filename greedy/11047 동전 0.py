n,k = map(int, input().split()) # n: 동전 종류수, k: 거스름돈

coins = [int(input()) for _ in range(n)]
coins.sort(reverse=True)
idx = 0
cnt = 0

while k > 0:
    if coins[idx] > k:
        idx += 1
    else:
        cnt += k//coins[idx]
        k %= coins[idx]
print(cnt)