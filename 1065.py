print(sum(i//100+i%10 == i//10%10*2 or i < 100 for i in range(1, int(input())+1)))
# why input() + 1 is used instead of input()?