from collections import deque

n, m = map(int, input().split())
ground = []
visited = []
queue = deque()

for i in range(n):
    row = list(map(int, input().strip()))
    ground.append(row)
    visited.append([(False, 987654321)] * m)

# 상하좌우 방향 벡터
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

# 초기 시작점 세팅
cnt = 1
visited[0][0] = (True, cnt)
queue.append((0, 0))

while queue:
    q_element = queue.popleft()
    i, j = q_element  # 현재 좌표
    cnt = visited[i][j][1]

    # 마지막 칸에 도달한 경우
    if i == n - 1 and j == m - 1:
        print(cnt)
        break

    # 상하좌우 탐색
    for k in range(4):
        ni, nj = i + di[k], j + dj[k]
        # 인덱스 범위 확인 및 이동 가능 여부 확인
        if 0 <= ni < n and 0 <= nj < m:
            if ground[ni][nj] == 1 and not visited[ni][nj][0]:
                queue.append((ni, nj))
                visited[ni][nj] = (True, cnt + 1)
