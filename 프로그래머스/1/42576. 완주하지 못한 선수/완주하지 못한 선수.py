def solution(participant, completion):
    playerList = {}
    
    for x in participant :
        if x not in playerList : playerList[x] = 1
        else : playerList[x] += 1
        
    for x in completion :
        playerList[x] -= 1
        
    for x in playerList :
        if playerList[x] == 1 : return x    

    
