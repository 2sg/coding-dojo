def d(n):
    return n + sum(map(int, str(n)))

# 10000 이하의 모든 숫자에 대해 d(n)을 계산
# 생성자가 있는 숫자들을 저장하기 위한 집합
generated = set()

# 1부터 10000까지 모든 숫자에 대해 d(n)을 계산하고 집합에 추가
for i in range(1, 10001):
    dn = d(i)
    if dn <= 10000:
        generated.add(dn)

# 1부터 10000까지 숫자 중에서 생성자가 없는 숫자를 출력
for i in range(1, 10001):
    if i not in generated:
        print(i)
