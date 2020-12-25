

import sys
N = int(sys.stdin.readline())
count = [0] * 10001
for i in range(N):
    count[int(sys.stdin.readline())] += 1

for j in range(len(count)):
    if count[j] != 0:
        for k in range(count[j]):
            print(j)

dic = {}
for i in range(N):
    a = int(sys.stdin.readline())

    if a in dic:
        dic[a] += 1
    else:
        dic[a] = 1

for j in sorted(dic.items()):
    for k in range(j[1]):
        print(j[0])