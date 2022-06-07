#1157번
s = input().lower()
word = list(set(s))
num = []

for i in word:
    nums = s.count(i)
    num.append(nums)
if num.count(max(num))>=2:
    print("?")
else:
    print(word[num.index(max(num))].upper())


    