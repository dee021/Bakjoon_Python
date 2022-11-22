def solution(n):
    if n == 1:
        return 1
    answer = 0
    for i in range(1, int(n**0.5)+1):
        if n%i == 0:
            answer += 1
    answer *= 2
    if int(n**0.5)**2 == n:
        answer -= 1
    return answer