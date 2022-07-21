t = int(input())

dp = [0 for i in range(12)]
dp[1], dp[2], dp[3] = 1, 2, 4

for i in range(4,12):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for i in range(t):
    print(dp[int(input())])
    
# sol
# n = 1 : 1 (1)
# n = 2 : 1+1 = 2 (2)
# n = 3 : 1+1+1 = 1+2 = 2+1 = 3 (4)
# n >= 4 :
#     모든 식은 1이나 2, 3으로 시작
#     - 1로 시작하는 경우 : (n-1)를 표현하는 식 앞에 1을 더함
#     - 2로 시작하는 경우 : (n-2)를 표현하는 식 앞에 2를 더함
#     - 3으로 시작하는 경우 : (n-3)를 표현하는 식 앞에 3을 더함
