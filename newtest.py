#script to progress bracket and store match info
import challonge
from challonge import api
challonge.set_credentials("halla", "BvQ5HZNCquhDuKZN544EHh27LEhlBnP0Kwxwlomf")


import json


def update(tournament, match_id, **params):
    #Update/submit the score(s) for a match.
    api.fetch(
        "PUT",
        "tournaments/%s/matches/%s" % (tournament, match_id),
        "match",
        **params)
def index(tournament):
    """Retrieve a tournament's participant list."""
    return api.fetch_and_parse(
        "GET",
        "tournaments/%s/participants" % tournament)

def matchlist(tournament, **params):
    """Retrieve a tournament's match list."""
    return api.fetch_and_parse(
        "GET",
        "tournaments/%s/matches" % tournament,
        **params)
    
with open('players.txt') as json_data:
    players=json.load(json_data)

#updating players json file to ocntain all players in a dict with keys from chalonge name
def playerlibupdate:
    for i in range(10):
        tournament_name="nyussbm%s" %i
        for j in index(tournament_name):
            if j not in players:
                players[j]={"Wins": [], "challonge-name":, "temp-id": {}, "Losses": [], "tag": }
    
#determining number of tournaments in the set and setting up tep ids for each one
a="nyussbm1"
c=int(input("what # tournament is this? Just enter the number!"))
a="nyussbm%s" %c
for i in players:
    if a not in players[i]["temp-id"]:
        players[i]["temp-id"][a] = 0
print("player profile updated")
print("loading")
        
#tourney name
partlist="nyussbm%s" %c
print(partlist)

#adding players without libraries to the big player lib
libupdate={"Wins": [], "tag": "", "Losses": [], "temp-id": {}, "challonge-name": ""}
for i in range(len(index(partlist))):
    if index(partlist)[i]["challonge-username"] not in players:
        tempname=index(partlist)[i]["challonge-username"]
        players[tempname]=libupdate
        players[tempname]["tag"]=tempname
        players[tempname]["challonge-name"]=tempname
with open('players.txt', 'w') as outfile:
    json.dump(players, outfile)


#determining temp id library for each tourney  
for j in players:
    for i in range(len(index(partlist))):
        if index(partlist)[i]["username"]==players[j]["challonge-name"]:
            players[j]["temp-id"][a]=index(partlist)[i]["id"]
                
with open('players.txt', 'w') as outfile:
    json.dump(players, outfile)

    

#updating matches gota make use of status to break a while loop later
#another problem is non nyu students because challonge names not in data base of players
#also problem with loop where while loop doesnt work properly
stat="notdone"
while stat != "done":
    matchidstart=int(matchlist(a)[1]["id"])
    matchidend=int(matchlist(a)[len(matchlist(a))-1]["id"])
    p1=input("enter which player's match you would like to enter. use challonge username please!")
    print("word")
    if p1=="done":
        break
    while p1 not in players:
        p1=input("Enter a valid player name")
    for i in range((matchidend-matchidstart+1)):
        if matchlist(a)[i]["player1-id"]==players[p1]["temp-id"][a] or matchlist(a)[i]["player2-id"]==players[p1]["temp-id"][a]:
            print("okay")
            if matchlist(a)[i]["state"] == "complete":
                print("completed match")
            elif matchlist(a)[i]["state"] == "open":
    #d1 turns in to challonge name
                d1=matchlist(a)[i]["player1-id"]
                d2=matchlist(a)[i]["player2-id"]
    #e2 stays as id number
                e1=matchlist(a)[i]["player1-id"]
                e2=matchlist(a)[i]["player2-id"]
                if d1==players[p1]["temp-id"][a]:
                    d1=p1
                    for j in players:
                        if players[j]["temp-id"][a]==d2:
                            d2=players[j]["challonge-name"]
                else:
                    if d2==players[p1]["temp-id"][a]:
                        d2=p1
                    for j in players:
                        if players[j]["temp-id"][a]==d1:
                            d1=players[j]["challonge-name"]
                print("player 1 is", d1,"and player 2 is", d2, ".", d1, "fought against", d2)
                w=input("who won the set (challonge name)")
                for k in players:
                    if players[k]["challonge-name"]==w:
                        cnamewinner=w
                        w=players[k]["temp-id"][a]
                gamecount=input("how many games was the set? enter 2, 3, 4, or 5.")
                g=[]
                if cnamewinner==d1:
                    setinfo={"set loser": d2, "set winner":d1, "game1":{}, "game2":{}, "game3":{}, "game4":{}, "game5":{}, "tournament id": a}
                elif cnamewinner==d2:
                    setinfo={"set loser": d1, "set winner":d2, "game1":{}, "game2":{}, "game3":{}, "game4":{}, "game5":{}, "tournament id": a}

                    
#clean up this part using loops
                
                if gamecount=="2":
                    g1=input("who won game 1")
                    setinfo["game1"]["winner"]=g1
                    g1stage=input("what stage was chosen for game 1?")
                    setinfo["game1"]["stage"]=g1stage
                    g1p1char=input("what character did player 1 choose?")
                    g1p2char=input("what character did player 2 choose?")
                    setinfo["game1"][d1]=g1p1char
                    setinfo["game1"][d2]=g1p2char
                    g2=input("who won game 2?")
                    setinfo["game2"]["winner"]=g2
                    g2stageban=input("what stage did ban? If no bans, enter none")
                    setinfo["game2"]["stage ban"]=g2stageban
                    g2stage=input("what stage was chosen for game 2?")
                    setinfo["game2"]["stage"]=g2stage
                    g2p1char=input("what character did player 1 choose?")
                    g2p2char=input("what character did player 2 choose?")
                    setinfo["game2"][d1]=g2p1char
                    setinfo["game2"][d2]=g2p2char
                    g.append(g1)
                    g.append(g2)
                    setinfo.pop("game3")
                    setinfo.pop("game4")
                    setinfo.pop("game5")
                    
                elif gamecount=="3":
                    g1=input("who won game 1")
                    setinfo["game1"]["winner"]=g1
                    g1stage=input("what stage was chosen for game 1?")
                    g1p1char=input("what character did player 1 choose?")
                    g1p2char=input("what character did player 2 choose?")
                    setinfo["game1"]["stage"]=g1stage
                    setinfo["game1"][d1]=g1p1char
                    setinfo["game1"][d2]=g1p2char
                    g2=input("who won game 2?")
                    setinfo["game2"]["winner"]=g2
                    g2stageban=input("what stage did ban? If no bans, enter none")
                    setinfo["game2"]["stageban"]=g2stageban
                    g2stage=input("what stage was chosen for game 2?")
                    setinfo["game2"]["stage"]=g2stage
                    g2p1char=input("what character did player 1 choose?")
                    g2p2char=input("what character did player 2 choose?")
                    setinfo["game2"][d1]=g2p1char
                    setinfo["game2"][d2]=g2p2char
                    g3=input("who won game 3")
                    setinfo["game3"]["winner"]=g3
                    g3stageban=input("what stage did ban? If no bans, enter none")
                    setinfo["game3"]["stageban"]=g3stageban
                    g3stage=input("what stage was chosen for game 3?")
                    setinfo["game3"]["stage"]=g3
                    g3p1char=input("what character did player 1 choose?")
                    g3p2char=input("what character did player 2 choose?")
                    setinfo["game3"][d1]=g3p1char
                    setinfo["game3"][d2]=g3p2char
                    g.append(g1)
                    g.append(g2)
                    g.append(g3)
                    setinfo.pop("game4")
                    setinfo.pop("game5")
                elif gamecount=="4":
                    g1=input("who won game 1")
                    setinfo["game1"]["winner"]=g1
                    g1stage=input("what stage was chosen for game 1?")
                    setinfo["game1"]["stage"]=g1stage
                    g1p1char=input("what character did player 1 choose?")
                    g1p2char=input("what character did player 2 choose?")
                    setinfo["game1"][d1]=g1p1char
                    setinfo["game1"][d2]=g1p2char
                    g2=input("who won game 2?")
                    setinfo["game2"]["winner"]=g2
                    g2stage=input("what stage was chosen for game 2?")
                    setinfo["game2"]["stage"]=g2stage
                    g2p1char=input("what character did player 1 choose?")
                    g2p2char=input("what character did player 2 choose?")
                    setinfo["game2"][d1]=g2p1char
                    setinfo["game2"][d2]=g2p2char
                    g3=input("who won game 3")
                    setinfo["game3"]["winner"]=g3
                    g3stage=input("what stage was chosen for game 3?")
                    setinfo["game3"]["stage"]=g3stage
                    g3p1char=input("what character did player 1 choose?")
                    g3p2char=input("what character did player 2 choose?")
                    setinfo["game3"][d1]=g3p1char
                    setinfo["game3"][d2]=g3p2char
                    g4=input("who won game 4")
                    setinfo["game4"]["winner"]=g4
                    g4stage=input("what stage was chosen for game 4?")
                    setinfo["game4"]["stage"]=g4stage
                    g4p1char=input("what character did player 1 choose?")
                    g4p2char=input("what character did player 2 choose?")
                    setinfo["game4"][d1]=g4p1char
                    setinfo["game4"][d2]=g4p2char
                    g.append(g1)
                    g.append(g2)
                    g.append(g3)
                    g.append(g4)
                    setinfo.pop("game5")
                elif gamecount=="5":
                    g1=input("who won game 1")
                    setinfo["game1"]["winner"]=g1
                    g1stage=input("what stage was chosen for game 1?")
                    setinfo["game1"]["stage"]=g1stage
                    g1p1char=input("what character did player 1 choose?")
                    g1p2char=input("what character did player 2 choose?")
                    setinfo["game1"][d1]=g1p1char
                    setinfo["game1"][d2]=g1p2char
                    g2=input("who won game 2?")
                    setinfo["game2"]["winner"]=g2
                    g2stage=input("what stage was chosen for game 2?")
                    setinfo["game2"]["stage"]=g2stage
                    g2p1char=input("what character did player 1 choose?")
                    g2p2char=input("what character did player 2 choose?")
                    setinfo["game2"][d1]=g2p1char
                    setinfo["game2"][d2]=g2p2char
                    g3=input("who won game 3")
                    setinfo["game3"]["winner"]=g3
                    g3stage=input("what stage was chosen for game 3?")
                    setinfo["game3"]["stage"]=g3stage
                    g3p1char=input("what character did player 1 choose?")
                    g3p2char=input("what character did player 2 choose?")
                    setinfo["game3"][d1]=g3p1char
                    setinfo["game3"][d2]=g3p2char
                    g4=input("who won game 4")
                    setinfo["game4"]["winner"]=g4
                    g4stage=input("what stage was chosen for game 4?")
                    setinfo["game4"]["stage"]=g4stage
                    g4p1char=input("what character did player 1 choose?")
                    g4p2char=input("what character did player 2 choose?")
                    setinfo["game4"][d1]=g4p1char
                    setinfo["game4"][d2]=g4p2char
                    g5=input("who won game 5")
                    setinfo["game5"]["winner"]=g5
                    g5stage=input("what stage was chosen for game 5?")
                    setinfo["game5"]["stage"]=g5stage
                    g5p1char=input("what character did player 1 choose?")
                    g5p2char=input("what character did player 2 choose?")
                    setinfo["game5"][d1]=g5p1char
                    setinfo["game5"][d2]=g5p2char
                    g.append(g1)
                    g.append(g2)
                    g.append(g3)
                    g.append(g4)
                    g.append(g5)
                if cnamewinner==d1:    
                    gnum=[]
                    gnum.append(str(g.count(cnamewinner)))
                    gnum.append("-")
                    gnum.append(str(len(g)-g.count(cnamewinner)))
                    gnumstr=''.join(gnum)
                    g=gnumstr
                    update(a, matchidstart+i-1, winner_id=w, scores_csv=g)
                    print("match updated!!")
                elif cnamewinner==d2:
                    gnum=[]
                    gnum.append(str(len(g)-g.count(cnamewinner)))
                    gnum.append("-")
                    gnum.append(str(g.count(cnamewinner)))
                    gnumstr=''.join(gnum)
                    g=gnumstr
                    update(a, matchidstart+i-1, winner_id=w, scores_csv=g)
#redo this section to add the dictionary instead of just the names
                if d1 in players:
                    if d2 in players:
                        if setinfo["set winner"]==d1:
                            players[d1]["Wins"].append(setinfo)
                            players[d2]["Losses"].append(setinfo)
                        elif setinfo["set winner"]== d2:
                            players[d2]["Wins"].append(setinfo)
                            players[d1]["Losses"].append(setinfo)
                        with open('players.txt', 'w') as outfile:
                            json.dump(players, outfile)
                        print("library updated!")
                        
                else:
                    print("match updated!")
                    print("one player not in data set, skipping archive")                    
                stat=input("are you sure you are done? If so, enter 'done' one more time!")
                break
            else:
                print("player has no matches")
                p1=input("When done entering all the matches, enter done! OR enter another players name.")
                if p1 == "done":
                    stat=input("are you sure you are done? If so, enter 'done' one more time!")
                
print("tournament finished!")

#Match Details now!"""

                        
