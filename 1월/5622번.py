#5622번

alpabets = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
num = input() #할머니의 입력값
time = 0 #걸리는 시간


for alpabet in alpabets: #알파벳 한 단위씩 읽기
    for i in alpabet:
        for j in num:
            if i == j:
                time += alpabets.index(alpabet) + 3
    

print(time)