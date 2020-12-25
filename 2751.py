#merge sort

import sys

def merge_sort(list):
    if len(list) <= 1:
        return list

    mid = len(list)//2
    left = merge_sort(list[:mid])
    right = merge_sort(list[mid:])
    return merge(left, right)

def merge(left, right):
    res = []
    while len(left) and len(right):
        if left[0] <= right[0]:
            res.append(left[0])
            del(left[0])
        else:
            res.append(right[0])
            del(right[0])
    if len(left): res = res + left
    if len(right): res = res + right

    return res

N = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(N)]
arr = merge_sort(arr)
# This print...
print(*arr, sep="\n")

