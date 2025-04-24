def circle_game(n):
    players = list(range(1, n + 1))
    judge_index = 0

    for k in range(1, n):
        judge_index = (judge_index + k) % len(players)

        players.pop(judge_index)

        judge_index = judge_index % len(players)

    return players[0]

print(circle_game(5))     
print(circle_game(125))  
print(circle_game(92))    
print(circle_game(789))   
