num_list = [0 for i in range(10001)] #리스트에 0으로 채우기
# 0이 소수임
num_list[1] = 1 

for i in range(2, 98):
    for j in range(i * 2, 10001, i):
        num_list[j] = 1
#2의 배수는 소수가 아니니까 1을 넣어줌

times = int(input())
for i in range(times):
    x = int(input())
    y = x // 2
    for j in range(y, 1, -1):
        if num_list[x - j] == 0 and num_list[j] == 0:
            print(j, x - j)
            break