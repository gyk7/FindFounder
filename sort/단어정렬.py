# 백준 1181번
N = int(input())
li = []

for i in range(N):
    M = input()
    li.append(M)
li = list(set(li))
li.sort(key = lambda x : (len(x),x))

for i in li:
    print(i)

