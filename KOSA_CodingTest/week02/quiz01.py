from collections import deque

def solution(maps):
    # 상하좌우 방향 벡터
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    # 행렬의 크기
    n = len(maps)
    m = len(maps[0])

    # 거리 및 방문 배열 (초기화: 방문하지 않은 상태는 0으로 표시)
    distance = [[0] * m for _ in range(n)]

    # BFS를 위한 큐 초기화
    case = deque()
    case.append((0, 0))
    distance[0][0] = 1  # 시작 지점은 거리 1로 시작

    # BFS 탐색 시작
    while case:
        i, j = case.popleft()

        # 목적지에 도착하면 거리 반환
        if i == n - 1 and j == m - 1:
            return distance[i][j]

        # 현재 위치에서 상하좌우 탐색
        for k in range(4):
            ii = i + di[k]
            jj = j + dj[k]

            # 맵의 범위를 벗어나지 않고, 벽이 아니며, 아직 방문하지 않은 경우
            if 0 <= ii < n and 0 <= jj < m and maps[ii][jj] == 1 and distance[ii][jj] == 0:
                distance[ii][jj] = distance[i][j] + 1
                case.append((ii, jj))

    # 도착할 수 없으면 -1 반환
    return -1
