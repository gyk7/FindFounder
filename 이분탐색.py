# programmers 입국심사
def solution(n, times):
    left = 0
    right = max(times) * n
 
    while left < right:
        mid = (left + right) // 2
        cnt = 0
 
        for i in times:
            cnt += mid // i
 
        if cnt >= n:
            right = mid
        else:
            left = mid + 1
 
    return left