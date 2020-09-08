num = int(input())
for i in range(num):
    R, S = input().split()
    R = int(R)
    # split : distinguish input value by blank
    S = str(S)
    for j in range(len(S)):
        print(R * S[j], end ='')
    print()