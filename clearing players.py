#clear wins and losses
import json
with open('players.txt') as json_data:
    players=json.load(json_data)


for i in players:
    players[i]["Wins"]=[]
    players[i]["Losses"]=[]
    print(players[i]["Wins"])
    print(players[i]["Losses"])
    
with open('players.txt', 'w') as outfile:
    json.dump(players, outfile)
                        
print("cleared wins and losses libraries!")
