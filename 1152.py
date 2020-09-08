str = list(input())
count = str.count(" ")
if str[0] == " " or str[-1] == " ":
    if str[0] == " " and str[-1] == " ":
        count -= 1
    else:
        pass
else:
    count += 1

print(count)