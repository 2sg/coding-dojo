current_positions = input()
row = int(current_positions[1])
column = ord(current_positions[0]) - ord('a') + 1

x = str(current_positions[0])
y = int(current_positions[1])

steps = [[-2, -1], [-2, 1], [2, -1], [2, 1], [-1, -2], [-1, 2], [1, -2], [1, 2]]

result = 0

# 이동 가능한 모든 경우의 수에 대해 반복
for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)

