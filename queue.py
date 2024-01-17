<<<<<<< HEAD
from sys import stdin
N = int(stdin.readline())
list =[]

for i in range(N):
    str = stdin.readline().split()
    
    if str[0] == "push":
        list.append(str[1])
    elif str[0] == "front":
        if len(str) == 0 :
            print(-1)
        else :
            print(list[0])
    elif str[0] == "back":
        if len(str) == 0 :
            print(-1)
        else :
            print(list[-1])
    elif str[0] == "size":
        print(len(list))
    elif str[0] == "pop" :
        if len(list) == 0 :
            print(-1)
        else :
            print(list[0])
            del(list[0])
    elif str[0] == "empty" :
        if len(list) == 0 :
            print(1)
        else :
            print(0)
    print(list)

import sys

N = int(sys.stdin.readline())

queue = []

for i in range(N):
    cmd = sys.stdin.readline().split()

    if cmd[0] == "push":
        queue.insert(0, cmd[1])
        ##print(queue)

    elif cmd[0] == "pop":
        if len(queue) != 0: print(queue.pop())
        else: print(-1)

    elif cmd[0] == "size":
        print(len(queue))

    elif cmd[0] == "empty":
        if len(queue) == 0: print(1)
        else : print(0)

    elif cmd[0] == "front":
        if len(queue) == 0: print(-1)
        else: print(queue[len(queue) -1])

    elif cmd[0] == "back":
        if len(queue) == 0: print(-1)
        else: print(queue[0])
=======
# 백준 - 10845번 큐
from sys import stdin
N = int(stdin.readline())
asdf =[]
result = []
for i in range(N):
    str_line = stdin.readline().split()
    
    if str_line[0] == "push":
        asdf.append(str_line[1])
    elif str_line[0] == "front":
        if len(asdf) == 0 :
            result.append(-1)
        else :
            result.append(int(asdf[0]))
    elif str_line[0] == "back":
        if len(asdf) == 0 :
            result.append(-1)
        else :
            result.append(int(asdf[-1]))
    elif str_line[0] == "size":
        result.append(len(asdf))
    elif str_line[0] == "pop" :
        if len(asdf) == 0 :
            result.append(-1)
        else :
            result.append(asdf[0])
            del(asdf[0])
    elif str_line[0] == "empty" :
        if len(asdf) == 0 :
            result.append(1)
        else :
            result.append(0)
            
print("\n".join(map(str,result)))
>>>>>>> b57926b8eed0a3ad5b6036960045e6d346ad2b71
