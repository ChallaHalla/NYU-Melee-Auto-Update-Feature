#analysis file
import json
with open('players.txt') as json_data:
    players=json.load(json_data)

selectedplayer=input("select a player")
path="head to head"
if path== "head to head":
    selectedplayer2=input("select another player")
    player1wins=0
    player2wins=0
    for i in range(len(players[selectedplayer]["Wins"])):
        if players[selectedplayer]["Wins"][i]["set loser"]==selectedplayer2:
            player1wins+=1
            print("Set Winner:", players[selectedplayer]["Wins"][i]['set winner'])
            print(selectedplayer, "played", players[selectedplayer]["Wins"][i]["game1"][selectedplayer])
            print(selectedplayer2, "played", players[selectedplayer]["Wins"][i]["game1"][selectedplayer2])
    for i in range(len(players[selectedplayer]["Losses"])):
        if players[selectedplayer]["Losses"][i]["set winner"]==selectedplayer2:
            player2wins+=1
            print("Set Winner:", players[selectedplayer]["Losses"][i]['set winner'])
            print(selectedplayer, "played", players[selectedplayer]["Losses"][i]["game1"][selectedplayer])
            print(selectedplayer2, "played", players[selectedplayer]["Losses"][i]["game1"][selectedplayer2])
    print("Their record is", player1wins, "-", player2wins)
    print("These players have played", player1wins+player2wins, "times")
            
