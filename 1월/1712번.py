#1712번.py

# 고정비용 A , 가변비용 B 컴퓨터가격 C 
# 

a,b,c = map(int,input().split()) 



if (c-b <= 0) :
    print("-1")
else:
    print(int((a/(c-b))+1))
