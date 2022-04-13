num = int(input())


books = {}


for i in range(num):
    book = str(input())

    if book in books.keys(): #책이 이미 저장 되어 있다면
        books[book] += 1
    else:  #없다면
        books[book] = 15

lists = []
for i in books.keys():
    if books[i] == max(books.values()):
        lists.append(i)
lists = sorted(lists)
print(lists[0])
    