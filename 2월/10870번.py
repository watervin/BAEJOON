#10870번 파이썬
# Fn = Fn-1 + Fn-2 (n ≥ 2)

fn = int(input())
sum = 0
num = [0,1]
for i in range(2,fn+1):
    num.append(num[i-1] + num[i-2])
print(num[fn])
 
    