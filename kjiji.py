from sys import stdin
N = int(stdin.readline())
list_g =[]

for i in range(N):
    str = stdin.readline().split()
    
    if str[0] == "push":
        list_g.append(str[1])
    elif str[0] == "front":
        if len(list_g) == 0 :
            print(-1)
        else :
            print(list_g[0])
    elif str[0] == "back":
        if len(list_g) == 0 :
            print(-1)
        else :
            print(list_g[-1])
    elif str[0] == "size":
        print(len(list_g))
    elif str[0] == "pop" :
        if len(list_g) == 0 :
            print(-1)
        else :
            print(list_g[0])
            del(list_g[0])
    elif str[0] == "empty" :
        if len(list_g) == 0 :
            print(1)
        else :
            print(0)