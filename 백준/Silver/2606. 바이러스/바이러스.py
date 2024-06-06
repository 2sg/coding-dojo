from collections import deque

computer_count = int(input())
network_count = int(input())
graph = [[] for _ in range(computer_count+1)] # 그래프 초기화
visited = [0] * (computer_count+1) # 방문 컴퓨터 표시

for i in range(network_count): # 그래프 생성
    a, b = map(int, input().split()) # 연결된 컴퓨터 입력
    graph[a].append(b) # 양방향 연결 - a에 b 연결
    graph[b].append(a) # 양방향 연결 - b에 a 연결

visited[1] = 1 # 1번 컴퓨터부터 시작이라 방문 표시

queue = deque([1])

while queue:
    v = queue.popleft()
    for i in graph[v]: # 연결된 컴퓨터 탐색
        if visited[i] == 0: # 방문하지 않은 컴퓨터라면
            queue.append(i) # 큐에 삽입
            visited[i] = 1

print(sum(visited)-1) # 1번 컴퓨터 제외한 방문한 컴퓨터 수 출력