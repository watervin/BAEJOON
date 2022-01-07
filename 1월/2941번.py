#2941번

cro_alpa = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
alpabet = input()
for i in range(len(cro_alpa)):
    if cro_alpa[i] in alpabet:
        alpabet = alpabet.replace(cro_alpa[i],"*")
print(len(alpabet))
