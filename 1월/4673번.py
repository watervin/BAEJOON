#4773번

num_list=[] #리스트 미리 만들어두기
def self_number(): #함수시작
    for i in range(1,10001): #다 돌려봐야함
        n = 0 #초기값
        if i<10: #1의 자리수
            n= i+i
            num_list.append(n)
        elif i<100: #10의 자리수
            n=i+(i//10)+(i%10) #//는 정수부분을 구하고 %몫을 구함
            num_list.append(n)
        elif i < 1000: #100의 자리수
            n = i+(i//100)+((i%100)//10)+((i%100)%10)
            num_list.append(n)
        elif i < 10000: #1000의 자리수
            n = i+(i//1000)+((i%1000)//100)+(((i%1000)%100)//10)+(((i%1000)%100)%10)
        if n <= 10000:
            num_list.append(n)
    result = set(num_list) #중복제거
    arr = [i for i in range(1,10001)]
    not_self = [num for num in arr if num not in result]
    
    for j in not_self:
        print(j)
self_number()
