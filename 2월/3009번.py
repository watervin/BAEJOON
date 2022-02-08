# 세 점이 주어졌을 때, 
# 축에 평행한 직사각형을 만들기 위해서 필요한 네 번째 점을 찾는 프로그램을 작성하시오.


num_list =[]
n_list = []
for i in range(3):
    num,n = map(int,input().split(" "))
    num_list.append(num)
    n_list.append(n)

for i in range(3):
    if num_list.count(num_list[i]) == 1:
        result1 = num_list[i]

    if n_list.count(n_list[i]) == 1:
        result2 = n_list[i]
print(result1,result2)

