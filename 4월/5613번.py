first = int(input())

while True :
  oper = input()
  if oper == '=' :
    break
  n = int(input())
  if oper == '+' :
    first += n
  elif oper == '-' :
    first -= n
  elif oper == '*' :
    first *= n
  else :
    first //= n

print(first)