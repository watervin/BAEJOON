num =int(input())
count = 0
for i in range(num):
    word = input()
    for j in range(len(word)-1):
        if word[j] != word[j+1]: #같지않은데
            if word[j] in word[j+1:]:
                count += 1
                break
print(count)
