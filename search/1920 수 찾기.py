n = int(input())
nlist = list(map(int, input().split()))
m = int(input())
mlist = list(map(int, input().split()))

for i in mlist:
    if i in nlist:
        print(1)
    else:
        print(0)