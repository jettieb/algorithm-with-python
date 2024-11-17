n = int(input())
m = int(input())

idx = list()
for i in range(n):
    for j in range(n):
        idx.append((i+1) * (j+1))

idx.sort()
print(idx[m])

"""
처음에 이렇게 작성했으나, 메모리초과 뜸. 그럴만함.. N이 10^5라 idx가 10^10이라서
"""

