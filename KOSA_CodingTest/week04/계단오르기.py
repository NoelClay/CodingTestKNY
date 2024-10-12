# # # 경우의수
# # 현재 값이 주어졌을때
# # 이전거+현재거 : 1개만 연속일때만 가능 -> 2개
# # 이이전거+현재거 : 제약 없음

# # 전부 한줄씩 띄워서 입력들어옴
# n = int(input())
# data = [int(input()) for _ in range(n)]

# dt = [0 for _ in range(n)]
# if n >= 0:
#   dt[0] = data[0]
# if n >= 1:
#   dt[1] = data[0] + data[1]
# # dt[2] = max(dt[0]+data[2], dt[1])
# # dt[3] = max(dt[1]+data[3], dt[2])

# if n >= 2:
#   for i in range(2, n):
#     dt[i] = max(dt[i - 2] + data[i], dt[i - 1])

# print(dt[n - 1])

# n = int(input())
# data = [int(input()) for _ in range(n)]

# dt = [0] * n

# if n >= 1:
#     dt[0] = data[0]
# if n >= 2:
#     dt[1] = data[0] + data[1]
# if n >= 3:
#     dt[2] = max(data[0] + data[2], data[1] + data[2], dt[1])

# for i in range(3, n):
#     dt[i] = max(
#         dt[i - 1],
#         dt[i - 2] + data[i],
#         dt[i - 3] + data[i - 1] + data[i]
#     )

# print(dt[n - 1])

n = int(input())
data = [int(input()) for _ in range(n)]

dt = [0] * n

if n >= 1:
    dt[0] = data[0]
if n >= 2:
    dt[1] = data[0] + data[1]
if n >= 3:
    dt[2] = max(data[0] + data[2], data[1] + data[2])

for i in range(3, n):
  # 마지막 계단을 무조건 밟아야된다는
    dt[i] = max(
        dt[i - 2] + data[i],
        dt[i - 3] + data[i - 1] + data[i]
    )

print(dt[n - 1])
