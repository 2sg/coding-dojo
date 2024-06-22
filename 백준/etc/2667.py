n = int(input())
graph = []
num = []
result = 0

for i in range(n):
    graph.append(list(map(int, input())))


def dfs(x, y):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    if graph[x][y] == 1:
        global count
        count += 1
        graph[x][y] = 0
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    return False

count = 0

for i in range(n):
    for j in range(n):
        if dfs(i, j):
            num.append(count)
            result += 1
            count = 0

num.sort()

print(result)
for i in range(len(num)):
    print(num[i])