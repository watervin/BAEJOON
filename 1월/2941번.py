#2941번

cro_alpa = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
alpabet = input()
count = 0
for i in range(len(cro_alpa)):
    if cro_alpa[i] in alpabet:
        count += 1
print(count)
