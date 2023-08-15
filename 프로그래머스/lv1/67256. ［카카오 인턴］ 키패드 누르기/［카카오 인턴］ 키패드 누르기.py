def solution(numbers, hand):
    # 키패드 위치 정의
    position = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2),
        '*': (3, 0), 0: (3, 1), '#': (3, 2)
    }
    
    # 초기 손 위치
    left = '*'
    right = '#'
    
    answer = ''
    
    for num in numbers:
        if num in [1, 4, 7]:  # 왼손 범위
            answer += 'L'
            left = num
        elif num in [3, 6, 9]:  # 오른손 범위
            answer += 'R'
            right = num
        else:  # 가운데 열
            l_x, l_y = position[left]
            r_x, r_y = position[right]
            n_x, n_y = position[num]
            
            l_distance = abs(n_x - l_x) + abs(n_y - l_y)
            r_distance = abs(n_x - r_x) + abs(n_y - r_y)
            
            if l_distance < r_distance:  # 왼손이 더 가까울 때
                answer += 'L'
                left = num
            elif l_distance > r_distance:  # 오른손이 더 가까울 때
                answer += 'R'
                right = num
            else:  # 거리가 같을 때
                if hand == "left":
                    answer += 'L'
                    left = num
                else:
                    answer += 'R'
                    right = num

    return answer