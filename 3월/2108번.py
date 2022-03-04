n = int(input())

lists = []
for _ in range(n) :
	lists.append(int(input()))

# 산술평균
print(round(sum(lists)/n))

# 중앙값
lists.sort()
print(lists[int((n-1)/2)])

# 최빈값
counts = dict()
for i in range(1,n+1) :
	counts[i] = []

max = 1
count = 1
for j in range(1,n) :
	if lists[j] == lists[j-1] :
		count += 1
	else :
		counts[count].append(lists[j-1])
		if max < count : max = count
		count = 1
	if j == n-1 : 
		counts[count].append(lists[j])
		if max < count : max = count

if n == 1 :
	counts[1].append(lists[0])

counts[max].sort()
if len(counts[max]) == 1 :
	print(counts[max][0])
else :
	print(counts[max][1])

# 범위
print(lists[-1]-lists[0])