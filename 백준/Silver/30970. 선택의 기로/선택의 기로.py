import sys
input = sys.stdin.readline

n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n)]
arr.sort(key = lambda x:(-x[0], x[1]))
print(*arr[0], *arr[1])
arr.sort(key=lambda x: (x[1], -x[0]))
print(*arr[0], *arr[1])