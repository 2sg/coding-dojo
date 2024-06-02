N = int(input())  # 전체 사람의 수 입력받기
people = []  # 사람들의 덩치 정보를 저장할 리스트

# 사람들의 덩치 정보 입력받기
for _ in range(N):
    weight, height = map(int, input().split())
    people.append((weight, height))

# 각 사람의 덩치 등수 구하기
ranks = []
for i in range(N):
    count = 0
    for j in range(N):
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            count += 1
    ranks.append(count + 1)

# 덩치 등수 출력하기
print(' '.join(map(str, ranks)))