import sys
input = sys.stdin.readline
output = sys.stdout.write

S = 0  # 초기 비트 마스크 설정, 모든 값은 비활성화된 상태

M = int(input().strip())  # 연산의 개수

for _ in range(M):
    line = input().strip().split()
    op = line[0]

    if op == "add":
        x = int(line[1])
        S |= (1 << (x - 1))
    elif op == "remove":
        x = int(line[1])
        S &= ~(1 << (x - 1))
    elif op == "check":
        x = int(line[1])
        output('1\n' if (S & (1 << (x - 1))) else '0\n')
    elif op == "toggle":
        x = int(line[1])
        S ^= (1 << (x - 1))
    elif op == "all":
        S = (1 << 20) - 1
    elif op == "empty":
        S = 0

# 각 `check` 연산 후에는 결과를 즉시 출력합니다. 다른 연산은 즉시 실행되며 결과를 저장하지 않습니다.
