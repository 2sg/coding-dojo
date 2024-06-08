from collections import deque

def solution(board):
    n, m = len(board), len(board[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # RIGHT, DOWN, LEFT, UP
    visited = [[False] * m for _ in range(n)]
    
    # 로봇(R) 위치와 목표(G) 위치 찾기
    start_x = start_y = goal_x = goal_y = None
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                start_x, start_y = i, j
            elif board[i][j] == 'G':
                goal_x, goal_y = i, j
    
    # BFS 초기화
    queue = deque([(start_x, start_y, 0)])  # (x, y, move_count)
    visited[start_x][start_y] = True
    
    # BFS 실행
    while queue:
        x, y, move_count = queue.popleft()
        
        if (x, y) == (goal_x, goal_y):
            return move_count
        
        for dx, dy in directions:
            nx, ny = x, y
            while True:
                nx += dx
                ny += dy
                if not (0 <= nx < n and 0 <= ny < m) or board[nx][ny] == 'D':
                    break
            nx -= dx
            ny -= dy
            if not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, move_count + 1))
    
    return -1  # 목표에 도달하지 못한 경우

