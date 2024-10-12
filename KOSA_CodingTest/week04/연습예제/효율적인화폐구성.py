# 무조건 더해서 원하는 타겟 넘버를 만드는 최소한의 경우의 수를 구하는 문제임.
# dfs를 이용해서 푸는 것보다 효율적인건 이미 이전 최적해가 있다면 그걸 이용하면 되기 때문임

# 첫째 줄에 입력 공백으로 2개 주어짐. 총 화폐의 개수 타겟 넘버
INF = 987654321
n, m = map(int, input().split())
# 그 다음은 줄바꿈으로 하나씩 배열의 요소가 주어짐.
data = [int(input()) for _ in range(n)]

# print(data)

dt = [INF for _ in range(10001)]

# 초기화
for d in data:
  dt[d] = 1

#타겟 넘버 만큼 반복함.
for i in range(m + 1):
  # print("i는" + str(i))
  # 후보해들 리스트야
  res = []
  for j in data:
    # print("j는" + str(j))
    #뺀 값이 범위 안에 들어온다면
    if i - j >= 0 and dt[i - j] != -1:
      # print("dt[i-j]는" + str(dt[i - j]))

      res.append(dt[i - j])
  # print("res는" + str(res))
    if res:
      dt[i] = min(res) + 1

print(dt[m])
