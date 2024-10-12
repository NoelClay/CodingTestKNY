# 총 1000개의 입력
N = int(input())

dt = [0 for _ in range(1001)]

dt[0] = 1
dt[1] = 3

for i in range(2, N):
  dt[i] = dt[i - 1] + dt[i - 2] * 2

print(dt[N - 1])
