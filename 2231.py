N = int(input())
min = 1000001
for i in range(N):
    value = i
    res = i
    while i:
        res += i % 10
        i //= 10
    if res == N and min > value:
        min = value

if min == 1000001:
    print(0)
else:
    print(min)