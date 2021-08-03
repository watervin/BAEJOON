#10871
cnt , num = map(int , input().split())
arr = list(map(int,input().split()))
for i in range(cnt):
    if arr[i] < num:
        print(arr[i],end=" ")
