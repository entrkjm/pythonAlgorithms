N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))
arr.sort()
for _ in range(len(arr)):
    print(arr[_])