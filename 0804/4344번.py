#4344번
num = int(input()) #몇번돌릴래

for i in range(num): #몇번돌릴래
    std_num = 0
    arr = list(map(int,input().split()))
    avg = (sum(arr)-arr[0])/arr[0] 
    for i in arr[1:]:
        if i > avg:
            std_num+=1
    over = std_num/arr[0]*100
    print('%.3f' %over + '%')


  