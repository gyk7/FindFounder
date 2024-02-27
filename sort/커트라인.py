N, k = map(int,input().split)
li = []

for i in range(N):
    x = int(input())
    li.append(x)

li.sort()
print(li[k-1])