import sys

N = int(sys.stdin.readline())
arr = []

for i in range(N):
    arr.append(int(sys.stdin.readline()))

arr = sorted(arr)

for i in arr:
    print(i)