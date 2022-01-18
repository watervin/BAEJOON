num = int(input())

for i in range(num):
    a = int(input()) #층
    b = int(input()) #호
    person_num = [j for j in range(1, b+1)] #컴프리핸션
    for j in range(a):
        for k in range(1,b):
            person_num[k] +=person_num[k-1]
    print(person_num[-1])

