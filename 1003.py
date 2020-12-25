#Fibonacci calling function is also follow Fibonacci series


def count(n):
    zero_count = [1, 0]
    one_count = [0, 1]
    if n <= 1:
        print(zero_count[n], one_count[n])
    else:
        for i in range(2, n+1):
            zero_count.append(zero_count[i-1] + zero_count[i-2])
            one_count.append(one_count[i-1] + one_count[i-2])
        print(zero_count[-1], one_count[-1])


T = int(input())
for i in range(T):
    N = int(input())
    count(N)



