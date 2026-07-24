def solution(players, callings):
    rank = {
        name: i
        for i, name in enumerate(players)
    }
    
    for call in callings:
        target_idx = rank[call] - 1
        front_player = players[target_idx]
        
        # player 순서 바꾸기
        players[rank[call]], players[target_idx] = front_player, call
        
        # rank 등수 바꾸기
        rank[front_player] += 1
        rank[call] -= 1
    
    return players
              
             