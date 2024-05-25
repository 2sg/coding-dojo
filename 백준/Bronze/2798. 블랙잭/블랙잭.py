def blackjack(N, M, cards):
    # 가장 가까운 합을 초기화
    closest_sum = 0

    # 모든 카드 3장 조합을 고려
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                current_sum = cards[i] + cards[j] + cards[k]
                # 현재 합이 M 이하이고, 이전에 찾은 가장 가까운 합보다 더 가깝다면 업데이트
                if current_sum <= M and current_sum > closest_sum:
                    closest_sum = current_sum

    return closest_sum

# 입력 받기
N, M = map(int, input().split())
cards = list(map(int, input().split()))

# 결과 출력
print(blackjack(N, M, cards))
