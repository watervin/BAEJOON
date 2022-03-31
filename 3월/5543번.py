#5543번
ham = []
coke = []

for i in range(3):
    money = int(input())
    ham.append(money)
for i in range(2):
    money = int(input())
    coke.append(money)

print(min(ham)+min(coke)-50)
