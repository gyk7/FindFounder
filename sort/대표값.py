li = []
sum = 0
for i in range(5):
    a = int(input())
    li.append(a)
li.sort()
for i in range(5):
    sum += li[i]

print(int(sum/5))
print(li[2])