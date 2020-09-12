N, K = map(int, input().split())
arr = list(map(int, input().split()))

val = 0
for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            if (K < (arr[i] + arr[j] + arr[k])):
                continue
            else:
                val = max(val, (arr[i]+arr[j]+arr[k]))
print(val)