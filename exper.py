import sys

sys.setrecursionlimit(100000) #런타임 에러 방지

n = int(input())

tree = [[] for _ in range(n+1)]

for _ in range(n-1): # 노드의 수 - 1 (간선)
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

parents = [0 for _ in range(n+1)]
parents[1] = 1


def dfs(curr, tree, parents):
    for node in tree[curr]:
        if parents[node] == 0:
            parents[node] = curr  # 해당 자식 노드에 부모노드(curr) 값 넣음
            dfs(node, tree, parents)  # 자식 노드가 서브 트리 루트로서 탐색

dfs(1, tree, parents)
print(*parents[2:])
