import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())
arr = sorted(list(map(int, sys.stdin.readline().split())))
for i in list(combinations(arr, m)):
    print(*i)