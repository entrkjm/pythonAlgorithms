str = list(input().upper())
alpha = [0] * 26

for i in str:
    alpha[ord(i)-65] += 1
# this grammer in for-loop is very simple
if alpha.count(max(alpha)) >= 2:
    print('?')
else:
    print(chr(alpha.index(max(alpha))+65))