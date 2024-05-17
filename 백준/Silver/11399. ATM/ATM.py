n = int(input())
times = list(map(int, input().split()))

times.sort()  # 인출 시간을 오름차순으로 정렬

total_time = 0  # 총 대기 시간
waiting_time = 0  # 누적 대기 시간

for time in times:
    waiting_time += time  # 현재 사람의 대기 시간 누적
    total_time += waiting_time  # 총 대기 시간에 누적

print(total_time)