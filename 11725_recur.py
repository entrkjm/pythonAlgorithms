# 이 풀이는 런타임 오류ㅠ 왜지

import sys

sys.setrecursionlimit(100000) #런타임 에러 방지

N = int(sys.stdin.readline())

Mat = [[] for i in range(N+1)]

parent = [0 for i in range(N+1)]


for i in range(N-1):
    v1, v2 = map(int, sys.stdin.readline().split())
    Mat[v1].append(v2)
    Mat[v2].append(v1)


def dfs(value, Mat, parent):
    for i in Mat[value]:
        parent[i] = value
        # Mat[value].remove(i) 이 값이 loop 자체에 영향을 미쳐버림.
        Mat[i].remove(value)
        dfs(i, Mat, parent)

parent[1] = 1
dfs(1, Mat, parent)

for i in range(2, N+1):
    print(parent[i])



