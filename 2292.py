num = int(input())
i = 1
seq = 1
if num == 1:
    print(1)
else:
    while(1):
        seq = seq + i * 6
        i += 1
        if(num <= seq):
            break
    print(i)