N = int(input())
li = []
for i in range(N) :
    a = int(input())
    li.append(a)

for i in range(N) :
    li.sort()
    print(li[i])