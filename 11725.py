# 트리를 직접 구현했었음

import sys

n = int(sys.stdin.readline())

class Node:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.child = []

def makeTree(node, arr, res):
    for i in range(len(arr[node.data])):
        if arr[node.data][i]:
            arr[i][node.data] = arr[node.data][i] = 0
            child = Node(i)
            node.child.append(child)
            child.parent = node
            res[child.data] = node.data

            makeTree(child, arr, res)


arr = [[0] * (n+1) for i in range(n+1)]

for i in range(n-1):
    v1, v2 = map(int, input().split())
    arr[v1][v2] = arr[v2][v1] = 1

res = [0 for i in range(n+1)]
node = Node(1)
makeTree(node, arr, res)

for i in range(2, n+1):
    print(res[i])



