#4673번
#어려움 ;; 못품
# 일단 리스트에 값 담기
arr = [ i for i in range(1,10001)]

def d(n): #일단 함수 만들기
  n=n+sum(map(int,str(n)))
  return n

#생성자가 있는지 확인할 리스트 초기화하기
a=[0]*10001

#생성자 찾기
for i in range(1,10001):
  a[i]=d(i)


for i in range(1,10001):
  #셀프넘버라면 출력하기
  if i not in a:
    print(i)