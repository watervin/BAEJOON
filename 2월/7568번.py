#7568번
num = int(input())
person_list = []
for i in range(num):
    w,h = map(int,input().split())
    person_list.append((w,h))

for i in person_list:
    one = 1
    for j in person_list:
        if i[0] < j[0] and i[1] < j[1]:
            one += 1
    print(one,end=" ")
