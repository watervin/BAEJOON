#2908번 
num1, num2 = input().split()
n1 = num1[::-1]
n2 = num2[::-1]
if n1 >n2 :
    print(n1)
else:
    print(n2)