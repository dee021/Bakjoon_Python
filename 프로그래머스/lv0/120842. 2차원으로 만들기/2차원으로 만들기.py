def solution(num_list, n):
    answer = [num_list[x:x+n] for x in range(0, len(num_list), n)]
    return answer