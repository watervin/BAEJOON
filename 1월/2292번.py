num = int(input()) #받을 숫자
count = 1 # 1부터시작
cnt_six = 1 #6개씩 늘어나는걸 셈

while num > cnt_six : # num =13
    cnt_six +=6 * count
    count += 1
    
    
print(count)
    
