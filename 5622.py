alpha = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
num = input().lower()
count = 0
for i in num:
    for j in alpha:
        if i in j:
            count += alpha.index(j) + 3
print(count)