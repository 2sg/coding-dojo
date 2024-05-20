from collections import deque

def bfs(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    visited = [[False] * cols for _ in range(rows)]
    queue = deque([(start[0], start[1], 1)])  # (row, col, distance)
    visited[start[0]][start[1]] = True
    
    while queue:
        row, col, distance = queue.popleft()
        
        if (row, col) == end:
            return distance
        
        # 상하좌우 이동
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        for dx, dy in directions:
            new_row, new_col = row + dx, col + dy
            
            if 0 <= new_row < rows and 0 <= new_col < cols and maze[new_row][new_col] == 1 and not visited[new_row][new_col]:
                queue.append((new_row, new_col, distance + 1))
                visited[new_row][new_col] = True
    
    return -1  # 도착 위치에 도달할 수 없는 경우

# 입력 받기
n, m = map(int, input().split())
maze = [list(map(int, input())) for _ in range(n)]

start = (0, 0)  # 시작 위치
end = (n - 1, m - 1)  # 도착 위치

min_distance = bfs(maze, start, end)
print(min_distance)