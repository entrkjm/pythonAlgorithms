S = input()
alpha = [-1] * 26

for i in range(len(S)):
    if alpha[ord(S[i])-97] != -1:
        continue
    else:
        alpha[ord(S[i])-97] = i

for i in range(26):
    print(alpha[i], end= ' ')