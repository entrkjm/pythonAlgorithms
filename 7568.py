N = int(input())
arr = [[0, 0] for _ in range(N)]
for i in range(N):
    arr[i] = list(map(int, input().split()))

rank = [0] * N

for i in range(N):
    count = 0
    for j in range(N):
        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            count += 1
    rank[i] = count + 1

for _ in range(0, N):
    print(rank[_], end=' ')