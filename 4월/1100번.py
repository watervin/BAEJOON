#1100번 하얀칸

lists =  []

for i in range(8):
    lists.append(list(map(str,list(input()))))

cnt = 0

for i in range(8):
    for j in range(8):
        if (i+j) %2 == 0:
            if lists[i][j] == 'F':
                cnt += 1
print(cnt)