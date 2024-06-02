"""
냉동실 얼음틀
구멍 뚫 1 안뚫 0
현재 틀을 기준으로 상, 하, 좌, 우에 연결되어 있는 경우 아이스크림으로 간주
"""

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))


def dfs(x, y):  # 깊이 우선 탐색. x, y: 방문하려는 노드의 좌표
    if x <= -1 or x >= n or y <= -1 or y >= m:  # 주어진 범위를 벗어나면 즉시 종료
        return False

    if graph[x][y] == 0:  # 현재 노드를 방문하지 않았다면
        graph[x][y] = 1  # 방문 처리
        dfs(x - 1, y)  # 상
        dfs(x + 1, y)  # 하
        dfs(x, y - 1)  # 좌
        dfs(x, y + 1)  # 우
        return True

    return False


result = 0

for i in range(n):
    for j in range(m):
        if dfs(i, j):
            result += 1
