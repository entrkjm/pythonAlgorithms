
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)

N = int(input())
print(factorial(N))