#2588번

n1 = int(input())
n2 = int(input())
res1 = n1 * ((n2%100)%10)
res2 = n1 * ((n2%100)//10)
res3 = n1 * ((n2//100))
sum =  n1 * n2
print(res1,res2,res3,sum,sep='\n')
