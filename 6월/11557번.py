#11557번.py

T = int(input())

dicts = {}
for i in range(T):
    name = str(input())
    value = int(input())
    dicts[name] = value

print(dicts)