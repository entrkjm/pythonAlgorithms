a, b = input().split()
#reverse method only is applied to list data type
#we need to declare list_a = list(a), list_a.reverse()

a = int(a[::-1])
b = int(b[::-1])

if (a > b):
    print(a)
else:
    print(b)