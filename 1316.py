#this code is not made by me

N = int(input())

res = 0

for i in range(N):
    word = input()
    for j in range(len(word)):
        if j != len(word) - 1:
            if word[j] == word[j+1]:
                continue
            else:
                if word[j] in word[j+1:]:
                    break

        else:
            res += 1
print(res)