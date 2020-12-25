import sys
from collections import Counter

N = int(sys.stdin.readline())

arr = []

for i in range(N):
    arr.append(int(sys.stdin.readline()))

def mean(parameter):
    return round(sum(parameter)/len(parameter))

# sum method와 len method를 활용한 mean 계산

def median(parameter):
    array = parameter
    array.sort()
    mid = len(array) // 2
    return array[mid]

# iterable type의 sort method를 활용

def mode(parameter):
    var = parameter
    var.sort()
    mode_dict = Counter(var)
    modes = mode_dict.most_common()

    # collection module의 counter, most_common method를 이용, 이 때 반환되는 type에 주의,
    # 최종 반환 type은 list
    # 여기서 most_common의 method는 최빈값이 여러 개인 경우, 원래 입력된 리스트의 순서대로 담음
    # 따라서 정렬을 해준다


    if  len(parameter) > 1:
        if modes[0][1] == modes[1][1]:
            mod = modes[1][0]
        else:
            mod = modes[0][0]
    else:
        mod = modes[0][0]

    return mod

def scope(arr):
    return max(arr) - min(arr)

print(mean(arr))
print(median(arr))
print(mode(arr))
print(scope(arr))


