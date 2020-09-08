alp = ['dz=', 'lj', 'nj', 'c=', 'c-', 'd-', 's=', 'z=']
sent = input()
count = 0

for i in alp:
    count += sent.count(i)
    sent = sent.replace(i, "_")

sent = sent.replace("_", "")
count += len(sent)
print(count)
