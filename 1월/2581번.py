#2581번 소수

num1 = int(input())
num2 = int(input())

nums_list=[]

   

for number in range(num1,num2+1):
    if number !=1:
        for i in range(2,number):
            if number % i ==0:
                break
        else :
            nums_list.append(number)
    

if len(nums_list)>0:
    print(sum(nums_list))
    print(min(nums_list))
else :
    print(-1)