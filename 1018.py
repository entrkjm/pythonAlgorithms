N, M = map(int, input().split())
a = []
val = []
for _ in range(N):
    a.append(input())

for i in range(N-7):
    for j in range(M-7):
        cnt1 = 0
        cnt2 = 0
        for k in range(i, i+8):
            for l in range(j, j+8):
                if(k+l) % 2 == 0:
                    if a[k][l] != "W":
                        cnt1 += 1
                    if a[k][l] != "B":
                        cnt2 += 1
                else:
                    if a[k][l] != "B":
                        cnt1 += 1
                    if a[k][l] != "W":
                        cnt2 += 1
        val.append(cnt1)
        val.append(cnt2)
print(min(val))