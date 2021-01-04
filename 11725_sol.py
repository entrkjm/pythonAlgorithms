import sys

N = int(sys.stdin.readline())

Mat = [[] for i in range(N+1)]

parent = [0 for i in range(N+1)]


for i in range(N-1):
    v1, v2 = map(int, sys.stdin.readline().split())
    Mat[v1].append(v2)
    Mat[v2].append(v1)


def dfs(input, Mat, parent):
    stack = [input]
    while stack:
        value = stack.pop()
        for i in Mat[value]:
            parent[i] = value
            stack.append(i)
            Mat[i].remove(value)

parent[1] = 1
dfs(1, Mat, parent)

for i in range(2, N+1):
    print(parent[i])



