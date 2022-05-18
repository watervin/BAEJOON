#10815번

import sys

input = sys.stdin.readline
N = int(input())
a_list = set(map(int,input().split()))
M = int(input())
b_list = list(map(int,input().split()))


for i in b_list : 
    if i in a_list:
        print(1 ,end = " ")
    else:
        print(0,end = " ")