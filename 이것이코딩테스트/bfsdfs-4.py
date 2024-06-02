"""
괴물 있 0 괴물 없 1
시작 위치 1, 1
출구 위치 n, m
탈출을 위해 움직여야 하는 최소 칸의 개수 result
"""
from collections import deque

n, m = map(int, input().split())

graph = []

for i in range(n):
    graph.append(list(map(int, input())))

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque()

    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4): # 현재 위치 기준으로 상하좌우 확인
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위 벗어나면 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            # 괴물 있으면 무시
            if graph[nx][ny] == 0:
                continue

            # 처음 방문하는 경우 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny)) # 큐에 삽입

    return graph[n - 1][m - 1] # 가장 오른쪽 아래까지의 최단 거리 반환