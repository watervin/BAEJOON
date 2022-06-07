#8958번
num = int(input())
sum=0
add = 1; 
for i in range(num):
    add = 1
    sum = 0 
    b = input()
    ox = list(b)
    for j in range(len(ox)):
        if (ox[j] == 'O'):
            sum += add
            add += 1
        else:
            add = 1; 
    print(sum)