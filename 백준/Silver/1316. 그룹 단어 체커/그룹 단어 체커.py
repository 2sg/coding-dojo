def is_group_word(word):
    last_seen = {}  # 각 문자의 마지막 위치를 저장
    for i, char in enumerate(word):
        if char in last_seen:
            if last_seen[char] != i - 1:  # 이전 등장 위치가 연속적이지 않다면
                return False
        last_seen[char] = i
    return True

def count_group_words(n, words):
    count = 0
    for word in words:
        if is_group_word(word):
            count += 1
    return count

# 입력 받기
n = int(input())
words = [input().strip() for _ in range(n)]

# 결과 출력
print(count_group_words(n, words))
