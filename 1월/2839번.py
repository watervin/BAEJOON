#봉다리는 3kg 5kg 존재
#먼저 3키로로 냅다 뺴야해 근데 5키로의 배수일때는 그게 좋음

n= int(input())
result = 0

while True:
    if n % 5 == 0:
        result +=(n // 5) # n을 5로 나눈 값 
        print(result)
        break
    n -=3 # 설탕무게에서 3씩 뺌
    result += 1 # 3키로 뺐으니 result 1추가
    if n==0:
        print(result)
        break
    if n<3:
         print("-1")
         break
