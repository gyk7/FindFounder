# 10845번
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