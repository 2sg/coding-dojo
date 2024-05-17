arr = list(map(int, input().split()))
n = arr[0]
k = arr[1]


value_list=[]
for i in range(n):
    value_list.append(int(input()))
value_list.sort(reverse=True)

"""
n은 동전의 종류
value_list는 각 동전이 가지고 있는 가치값의 list
k값을 합산하여 맞추기 위해 필요한 동전 종류의 개수의 최소값 나타내기

1. value_list를 내림차순으로 정렬한다.
2. 가장 큰 가치의 동전부터 k값을 나누어 몫을 구한다.
3. 몫을 result에 더하고, k값을 나머지로 초기화한다.
4. k값이 0이 되면 break한다.
5. 반복한 횟수는 필요한 동전 개수가 된다 동전 개수를 출력한다

"""

value_list.sort(reverse=True)
result = 0

for i in value_list:
    if k == 0:
        break
    result += k // i
    k %= i

print(result)


