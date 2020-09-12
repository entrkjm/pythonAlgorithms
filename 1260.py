N, M, V = map(int, input().split())
matrix = [[0]*(N+1) for _ in range(N+1)]

for _ in range(M):
    i, j = map(int, input().split())
    matrix[i][j] = 1
    matrix[j][i] = 1

visit = [0]*(N+1)

def dfs(V):
    visit[V] = 1
    print(V, end = " ")
    for i in range(1, N+1):
        if visit[i] == 0 and matrix[V][i] == 1:
            dfs(i)

def bfs(V):
    queue = [V]
    visit[V] = 0
    while queue:
        t = queue.pop(0)
        print(t, end = " ")
        for i in range(1, N+1):
            if(visit[i] == 1 and matrix[t][i] == 1):
                queue.append(i)
                visit[i] = 0


dfs(V)
print()
bfs(V)