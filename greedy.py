# 백준 그리디 2720번
from sys import stdin
T = int(stdin.readline())
q = 25
d = 10
n = 5
p = 1
for i in range(T) :
    M = int(stdin.readline())
    print(M // q, M % q // d, M % q % d // n, M % q % d % n // p)