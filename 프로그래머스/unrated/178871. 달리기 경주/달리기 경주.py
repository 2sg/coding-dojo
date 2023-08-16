def solution(players, callings):
    # 선수의 이름을 key로, 등수를 value로 하는 딕셔너리를 생성합니다.
    rank_dict = {player: rank for rank, player in enumerate(players)}
    
    for calling in callings:
        # 해당 선수의 현재 등수를 가져옵니다.
        current_rank = rank_dict[calling]
        
        # 추월하기 전 선수의 이름을 가져옵니다.
        prev_player = players[current_rank - 1]
        
        # 두 선수의 등수를 변경합니다.
        rank_dict[calling] -= 1
        rank_dict[prev_player] += 1
        
        # players 리스트에서 두 선수의 위치를 변경합니다.
        players[current_rank - 1], players[current_rank] = players[current_rank], players[current_rank - 1]
    
    return players