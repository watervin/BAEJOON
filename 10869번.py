#10869번
A,B=input().split()
A=int(A)
B=int(B)
if A>=1 and B<=10000:
    print(A+B)
    print(A-B)
    print(A*B)
    print(A//B)
    print(A%B)