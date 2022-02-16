#2480번
#같은 눈이 3개가 나오면 10,000원+(같은 눈)×1,000원의 상금을 받게 된다. 
#같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)×100원의 상금을 받게 된다. 
#모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)×100원의 상금을 받게 된다.

a,b,c = map(int,input().split())
a_list = [a,b,c]
a_list.sort()

if a_list[0] == a_list[1] == a_list[2]:
    print(10000+a_list[0]*1000)
elif a_list[0] == a_list[1]:
    print(1000+a_list[0]*100)
elif a_list[1] == a_list[2]:
    print(1000+a_list[1]*100)
elif a_list[2] == a_list[0]:
    print(1000+a_list[2]*100)
else:
    print(a_list[2]*100) 
