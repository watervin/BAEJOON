import sys

sentence = sys.stdin.read()
alph = 'abcdefghijklmnopqrstuvwxyz'
result = [] 

for i in alph:
   result.append(sentence.count(i))

max_num = max(result)
for i in range(len(result)):
    if max_num == result[i]:
            print(chr(i+97), end='')