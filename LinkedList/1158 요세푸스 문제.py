# 배열로 원형큐 만들어서 문제 풀이

n,k = map(int, input().split())
a = list(range(1,n+1))
index = 0
result = []

while a:
    index = (index + k - 1) % len(a)
    result.append(str(a.pop(index)))

print("<", end='')
print(", ".join(result), end='')
print(">", end='')