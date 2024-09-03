#n m
#각 행렬을 채울 리스트가 쫙 입력됨.

#n*m의 자료를 담을 녀석을 만들어야함.
n, m = map(int, input().split())
ground = []
for i in range(n):
  row = list(map(int, input().split()))
  ground.append(row)

#반복문 쫙 돌릴건데, 여기서 반복문 시작할때
#딱 처음 0을 만날때만 전체 result++

#후보체크기능
#현재 좌표가 0이야? 참
#  참이면 해당 좌료값 1로 바꾸고 상하좌우 싹 다 체크체크체크체크
# 인덱스아웃 아니면서, 해당값이 0이면 '후보체크(재귀)'
# 인덱스아웃 이거나, 해당값이 1이면 걍 리턴
#후보체크기능에서 호출호출호출호출이 완전히 종료가 되면 1덩어리가 만들어져 있을거임.

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]


#다시 0을 찾아 삼만리
def recursionDFS(i, j):
  global ground
  ground[i][j] = 1
  #상하좌우 후보자식 호출하기 위해 검사하는 로직 여기에 넣어야함.
  for k in range(4):
    #아웃오브 인덱스 체크
    if i + di[k] < 0 or i + di[k] >= n or j + dj[k] < 0 or j + dj[k] >= m:
      continue
    # 0이면 후보 추가 즉 참을 반환하면 될듯
    elif ground[i + di[k]][j + dj[k]] == 0:
      recursionDFS(i + di[k], j + dj[k])


result = 0

#요게 메인 로직
for i in range(n):
  for j in range(m):
    if ground[i][j] == 0:
      #첫번째 0의 희생양을 찾았다면 cnt를 증가시키고 ground를 1로 바꾸고 이자식을 기반으로 재귀
      #이자리에 재귀 호출의 시작을 넣어야함.
      result += 1
      recursionDFS(i, j)

print(result)
